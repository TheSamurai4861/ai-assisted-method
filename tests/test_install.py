"""Safety checks for installing into an existing project."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


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
        self.assertIn("(0 changes)", second.stdout)

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

    def test_conflict_stops_before_any_change(self):
        (self.project / "AGENTS.md").write_text("# Existing rules\n", encoding="utf-8")
        (self.project / ".ai").mkdir()
        (self.project / ".ai" / "METHOD.md").write_text("Local method\n", encoding="utf-8")

        result = self.run_installer()
        self.assertEqual(result.returncode, 1)
        self.assertIn("no files were changed", result.stderr)
        self.assertEqual((self.project / "AGENTS.md").read_text(), "# Existing rules\n")
        self.assertFalse((self.project / ".ai" / "SECURITY.md").exists())
        self.assertFalse((self.project / "prompts").exists())

    def test_dry_run_does_not_write(self):
        result = self.run_installer("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.project.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
