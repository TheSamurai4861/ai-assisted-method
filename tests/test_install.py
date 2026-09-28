"""Safety checks for installing into an existing project."""

from contextlib import redirect_stdout
from pathlib import Path
import importlib.util
import io
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.py"


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix=".install-test-", dir=ROOT)
        self.addCleanup(self.temporary.cleanup)
        self.project = Path(self.temporary.name) / "project"
        self.project.mkdir()

    def run_installer(self, *args):
        return subprocess.run(
            [sys.executable, str(INSTALLER), *args],
            cwd=self.project,
            capture_output=True,
            text=True,
            input="",
            check=False,
        )

    def test_clean_project_and_repeat_run(self):
        first = self.run_installer()
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(
            (self.project / "AGENTS.md").read_bytes(), (ROOT / "AGENTS.md").read_bytes()
        )
        self.assertTrue((self.project / ".ai" / "METHOD.md").is_file())
        self.assertTrue((self.project / "prompts" / "start-task.md").is_file())

        second = self.run_installer()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn("Planned changes: 0", second.stdout)

    def test_existing_rules_are_preserved_and_linked_once(self):
        original = b"# Existing project rules\r\n\r\nKeep the API stable.\r\n"
        (self.project / "AGENTS.md").write_bytes(original)
        (self.project / "CLAUDE.md").write_text("Local instructions.\n", encoding="utf-8")
        (self.project / ".ai").mkdir()
        (self.project / ".ai" / "LOCAL.md").write_text("Local rule.\n", encoding="utf-8")

        self.assertEqual(self.run_installer().returncode, 0)
        self.assertEqual(self.run_installer().returncode, 0)
        installed = (self.project / "AGENTS.md").read_bytes()
        self.assertTrue(installed.startswith(original))
        self.assertEqual(installed.count(b"<!-- ai-assisted-engineering-method:start -->"), 1)
        self.assertNotIn(b"\n", installed.replace(b"\r\n", b""))
        self.assertEqual(
            (self.project / "CLAUDE.md").read_text(encoding="utf-8"), "Local instructions.\n"
        )
        self.assertEqual(
            (self.project / ".ai" / "LOCAL.md").read_text(encoding="utf-8"), "Local rule.\n"
        )

    def test_conflict_offers_modes_without_changing_files(self):
        (self.project / "AGENTS.md").write_text("# Existing rules\n", encoding="utf-8")
        (self.project / ".ai").mkdir()
        (self.project / ".ai" / "METHOD.md").write_text("Local method\n", encoding="utf-8")

        result = self.run_installer()
        self.assertEqual(result.returncode, 2)
        self.assertIn("--mode update", result.stdout)
        self.assertIn("--mode separate", result.stdout)
        self.assertIn("--mode replace", result.stdout)
        self.assertEqual((self.project / "AGENTS.md").read_text(), "# Existing rules\n")
        self.assertFalse((self.project / ".ai" / "SECURITY.md").exists())
        self.assertFalse((self.project / "prompts").exists())

    def test_separate_mode_preserves_root_method_and_rewrites_references(self):
        (self.project / "AGENTS.md").write_text("# Project rules\n", encoding="utf-8")
        (self.project / ".ai").mkdir()
        (self.project / ".ai" / "METHOD.md").write_text("Another method\n", encoding="utf-8")

        first = self.run_installer("--mode", "separate")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual((self.project / ".ai" / "METHOD.md").read_text(), "Another method\n")
        staged = self.project / ".ai" / "ai-assisted-method"
        self.assertTrue((staged / "METHOD.md").is_file())
        self.assertIn(
            ".ai/ai-assisted-method/METHOD.md",
            (staged / "prompts" / "start-task.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            ".ai/ai-assisted-method/",
            (self.project / "AGENTS.md").read_text(encoding="utf-8"),
        )
        second = self.run_installer("--mode", "separate")
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn("Planned changes: 0", second.stdout)

    def test_update_preserves_project_facts_and_backs_up_method(self):
        (self.project / ".ai").mkdir()
        old_method = b"# AI-Assisted Development Method\nLocal rule.\n"
        (self.project / ".ai" / "METHOD.md").write_bytes(old_method)
        (self.project / ".ai" / "PROJECT_MAP.md").write_text("Observed app facts\n")
        (self.project / ".ai" / "VERIFICATION.md").write_text("Real checks\n")
        (self.project / ".ai" / "SECURITY.md").write_text("Local security rule\n")
        (self.project / ".ai" / "TASK_TEMPLATE.md").write_text("Local task template\n")

        result = self.run_installer("--mode", "update")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (self.project / ".ai" / "METHOD.md").read_bytes(),
            (ROOT / ".ai" / "METHOD.md").read_bytes(),
        )
        self.assertEqual((self.project / ".ai" / "PROJECT_MAP.md").read_text(), "Observed app facts\n")
        self.assertEqual((self.project / ".ai" / "VERIFICATION.md").read_text(), "Real checks\n")
        self.assertEqual(
            (self.project / ".ai" / "SECURITY.md").read_bytes(),
            (ROOT / ".ai" / "SECURITY.md").read_bytes(),
        )
        backups = list((self.project / ".ai" / "ai-assisted-method-backups").glob("*/.ai/METHOD.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), old_method)
        self.assertEqual((backups[0].parent / "SECURITY.md").read_text(), "Local security rule\n")
        self.assertTrue((self.project / ".ai" / "ai-assisted-method-backups" / ".gitignore").is_file())

    def test_interactive_menu_accepts_separate_choice(self):
        spec = importlib.util.spec_from_file_location("method_installer", INSTALLER)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with patch.object(module.sys, "stdin") as stdin, patch("builtins.input", return_value="2"), redirect_stdout(io.StringIO()):
            stdin.isatty.return_value = True
            mode = module.choose_mode([Path(".ai/METHOD.md")], SimpleNamespace(mode=None, dry_run=False))
        self.assertEqual(mode, "separate")

    def test_separate_mode_updates_only_its_existing_agent_block(self):
        spec = importlib.util.spec_from_file_location("method_installer", INSTALLER)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        (self.project / "AGENTS.md").write_text(
            "# Project rules\n\nKeep the API stable.\n\n" + module.LEGACY_BRIDGE,
            encoding="utf-8",
        )
        (self.project / ".ai").mkdir()
        (self.project / ".ai" / "METHOD.md").write_text("Another method\n")

        result = self.run_installer("--mode", "separate")
        self.assertEqual(result.returncode, 0, result.stderr)
        updated = (self.project / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Keep the API stable.", updated)
        self.assertEqual(updated.count("<!-- ai-assisted-engineering-method:start -->"), 1)
        self.assertIn(".ai/ai-assisted-method/", updated)
        self.assertNotIn("Read `.ai/METHOD.md`", updated)

    def test_replace_backs_up_and_overwrites_conflicts(self):
        (self.project / ".ai").mkdir()
        (self.project / ".ai" / "METHOD.md").write_text("Other method\n")
        (self.project / ".ai" / "PROJECT_MAP.md").write_text("Local map\n")

        result = self.run_installer("--mode", "replace")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (self.project / ".ai" / "PROJECT_MAP.md").read_bytes(),
            (ROOT / ".ai" / "PROJECT_MAP.md").read_bytes(),
        )
        backups = list((self.project / ".ai" / "ai-assisted-method-backups").glob("*/.ai/PROJECT_MAP.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), "Local map\n")

    def test_dry_run_does_not_write(self):
        result = self.run_installer("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.project.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
