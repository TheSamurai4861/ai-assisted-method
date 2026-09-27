"""Check the public methodology repository without third-party dependencies."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "LICENSE", "pyproject.toml",
    ".ai/METHOD.md", ".ai/PROJECT_MAP.md",
    ".ai/TASK_TEMPLATE.md", ".ai/VERIFICATION.md", ".ai/REVIEW_TEMPLATE.md",
    ".ai/SECURITY.md", ".ai/workflows/FEATURE.md", "prompts/start-task.md",
    "examples/BUGFIX_EXAMPLE.md", "examples/FEATURE_EXAMPLE.md",
    "examples/INVESTIGATION_EXAMPLE.md", "examples/MAINTENANCE_EXAMPLE.md",
    "examples/MIGRATION_EXAMPLE.md", "examples/INSTALLER_CASE_STUDY.md",
    "scripts/install.py",
    ".github/workflows/validate.yml", "tests/test_install.py",
]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ROOT_REFERENCE = re.compile(r"(?<![\w/])(?:\.ai|prompts|examples|scripts)/[A-Za-z0-9_./-]+")
errors = []

for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f"Missing required file: {name}")

for doc in ROOT.rglob("*.md"):
    if ".git" in doc.parts or doc.name == "PREP_REPORT.md":
        continue
    content = doc.read_text(encoding="utf-8")
    for target in LINK.findall(content):
        path = unquote(target.split("#", 1)[0])
        if not path or "://" in path or path.startswith("mailto:"):
            continue
        if not (doc.parent / path).exists():
            errors.append(f"Broken link: {doc.relative_to(ROOT)} -> {target}")
    for reference in ROOT_REFERENCE.findall(content):
        reference = reference.rstrip(".")
        if not (ROOT / reference).exists():
            errors.append(f"Missing repository reference: {doc.relative_to(ROOT)} -> {reference}")

for old in (ROOT / "prompts").glob("[0-9][0-9]_*"):
    errors.append(f"Old numbered prompt remains: {old.relative_to(ROOT)}")

for forbidden in ("method.zip", "_method_audit"):
    if (ROOT / forbidden).exists():
        errors.append(f"Extraction artifact in repository: {forbidden}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Repository structure and local Markdown links: OK")
