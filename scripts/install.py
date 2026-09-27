"""Install the method from an adopter's project without replacing its rules."""

import argparse
from pathlib import Path
import shutil
import sys


DIRECTORY = Path(__file__).resolve().parent
SOURCE = DIRECTORY.parent if (DIRECTORY.parent / "AGENTS.md").is_file() else DIRECTORY / "templates"
START = "<!-- ai-assisted-engineering-method:start -->"
END = "<!-- ai-assisted-engineering-method:end -->"
BRIDGE = f"""{START}
## AI-Assisted Engineering Method

Read `.ai/METHOD.md` for the task lifecycle, `.ai/SECURITY.md` for sensitive actions,
and `.ai/VERIFICATION.md` for checks. Continue to follow the existing project rules
in this file and other repository instructions. If a generic method rule conflicts
with a project rule, surface the conflict for human resolution before acting.
{END}
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install the method into the current project (or a given directory)."
    )
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()
    target = args.project.resolve()

    if not target.is_dir():
        parser.error("The target project directory must already exist.")
    if target == SOURCE:
        parser.error("Run this command from the project adopting the method.")

    method_files = sorted(
        p for directory in (".ai", "prompts")
        for p in (SOURCE / directory).rglob("*") if p.is_file()
    )
    if not method_files or not (SOURCE / "AGENTS.md").is_file():
        parser.error("The method source is incomplete.")

    actions = []
    conflicts = []
    for directory in (".ai", ".ai/workflows", "prompts"):
        destination = target / directory
        if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
            conflicts.append(f"Cannot use directory: {destination}")
    for source in method_files:
        destination = target / source.relative_to(SOURCE)
        if target not in destination.resolve().parents:
            conflicts.append(f"Path escapes target: {destination}")
        elif destination.is_symlink():
            conflicts.append(f"Symlink destination: {destination}")
        elif destination.exists():
            if not destination.is_file() or destination.read_bytes() != source.read_bytes():
                conflicts.append(f"Different existing file: {destination}")
        else:
            actions.append(("copy", source, destination))

    agents = target / "AGENTS.md"
    if agents.is_symlink():
        conflicts.append(f"Symlink destination: {agents}")
    elif agents.exists():
        if not agents.is_file():
            conflicts.append(f"Not a file: {agents}")
        else:
            try:
                current = agents.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                conflicts.append(f"AGENTS.md is not UTF-8: {agents}")
            else:
                if (START in current) != (END in current):
                    conflicts.append(f"Incomplete method block: {agents}")
                elif START not in current and agents.read_bytes() != (SOURCE / "AGENTS.md").read_bytes():
                    actions.append(("append", None, agents))
    else:
        actions.append(("copy", SOURCE / "AGENTS.md", agents))

    if conflicts:
        print("Installation stopped; no files were changed:", file=sys.stderr)
        for conflict in conflicts[:10]:
            print(f"  {conflict}", file=sys.stderr)
        if len(conflicts) > 10:
            print(f"  ... and {len(conflicts) - 10} more", file=sys.stderr)
        print("Resolve these conflicts manually, then rerun the command.", file=sys.stderr)
        return 1

    if args.dry_run:
        print(f"Would make {len(actions)} changes in {target}:")
        for operation, _, destination in actions:
            print(f"  {operation}: {destination.relative_to(target)}")
        return 0

    for operation, source, destination in actions:
        if operation == "copy":
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        else:
            existing = destination.read_bytes()
            newline = b"\r\n" if b"\r\n" in existing else b"\n"
            prefix = b"" if existing.endswith((b"\n", b"\r")) else newline
            with destination.open("ab") as file:
                file.write(prefix + newline + BRIDGE.replace("\n", newline.decode()).encode())

    print(f"Installed method in {target} ({len(actions)} changes).")
    print("Existing project rules were preserved. Review any rule conflicts.")
    print("Next: ask your coding agent to apply prompts/bootstrap-new-project.md.")
    print("Review rule conflicts, .ai/PROJECT_MAP.md, and .ai/VERIFICATION.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
