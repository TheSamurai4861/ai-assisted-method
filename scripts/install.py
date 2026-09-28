"""Install the method while preserving existing project instructions."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys


DIRECTORY = Path(__file__).resolve().parent
SOURCE = DIRECTORY.parent if DIRECTORY.name == "scripts" else DIRECTORY / "templates"
NAMESPACE = Path(".ai") / "ai-assisted-method"
PROJECT_FILES = {Path(".ai/PROJECT_MAP.md"), Path(".ai/VERIFICATION.md")}
START = "<!-- ai-assisted-engineering-method:start -->"
END = "<!-- ai-assisted-engineering-method:end -->"
LEGACY_BRIDGE = f"""{START}
## AI-Assisted Engineering Method

Read `.ai/METHOD.md` for the task lifecycle, `.ai/SECURITY.md` for sensitive actions,
and `.ai/VERIFICATION.md` for checks. Continue to follow the existing project rules
in this file and other repository instructions. If a generic method rule conflicts
with a project rule, surface the conflict for human resolution before acting.
{END}
""".lstrip()


def bridge(separate: bool) -> str:
    if not separate:
        return LEGACY_BRIDGE
    return f"""{START}
## AI-Assisted Engineering Method

A separate copy is staged in `.ai/ai-assisted-method/`. Read its `METHOD.md`,
`SECURITY.md`, and `VERIFICATION.md` alongside the existing project rules.
Start with `.ai/ai-assisted-method/prompts/bootstrap-new-project.md`.
Do not treat this copy as replacing existing rules. Surface consequential
differences for human resolution before changing the project's direction.
{END}
""".lstrip()


def destination_for(relative: Path, separate: bool) -> Path:
    if not separate:
        return relative
    if relative.parts[0] == ".ai":
        return NAMESPACE.joinpath(*relative.parts[1:])
    return NAMESPACE.joinpath("prompts", *relative.parts[1:])


def incoming_bytes(source: Path, separate: bool) -> bytes:
    if not separate:
        return source.read_bytes()
    return source.read_text(encoding="utf-8").replace(
        ".ai/", ".ai/ai-assisted-method/"
    ).encode("utf-8")


def agent_change(current: bytes | None, separate: bool) -> tuple[bytes | None, str | None]:
    desired = bridge(separate)
    if current is None:
        if separate:
            return ("# Agent entrypoint\n\n" + desired).encode("utf-8"), None
        return (SOURCE / "AGENTS.md").read_bytes(), None
    if current == (SOURCE / "AGENTS.md").read_bytes() and not separate:
        return None, None

    newline = b"\r\n" if b"\r\n" in current else b"\n"
    start = current.find(START.encode())
    end = current.find(END.encode())
    if (start >= 0) != (end >= 0):
        return None, "Incomplete managed block in AGENTS.md; review it manually."
    if start >= 0:
        end += len(END)
        current_block = current[start:end].decode("utf-8", errors="replace").replace("\r\n", "\n")
        known = {bridge(False).strip(), bridge(True).strip()}
        if current_block not in known:
            return None, "Customized managed block in AGENTS.md was preserved; review its path."
        replacement = desired.strip().replace("\n", newline.decode()).encode("utf-8")
        updated = current[:start] + replacement + current[end:]
        return (updated if updated != current else None), None

    prefix = b"" if current.endswith((b"\n", b"\r")) else newline
    addition = desired.replace("\n", newline.decode()).encode("utf-8")
    return current + prefix + newline + addition, None


def choose_mode(conflicts: list[Path], args: argparse.Namespace) -> str | None:
    if args.mode:
        return args.mode
    if not conflicts:
        return "normal"
    print(f"Found {len(conflicts)} existing files with different content:")
    for path in conflicts[:8]:
        print(f"  {path}")
    if len(conflicts) > 8:
        print(f"  ... and {len(conflicts) - 8} more")
    print("Choose how to proceed:")
    print("  1. Update current method: back up rules (including security); keep project map and verification.")
    print("  2. Install separately: preserve everything under .ai/ai-assisted-method/.")
    print("  3. Replace method files: back up and overwrite all matching paths, including project settings.")
    print("  4. Cancel.")
    if args.dry_run or not sys.stdin.isatty():
        print("Rerun with --mode update, --mode separate, or --mode replace.")
        return None
    try:
        choice = input("Choice [1-4]: ").strip()
    except EOFError:
        return None
    return {"1": "update", "2": "separate", "3": "replace"}.get(choice)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install the method into the current project (or a given directory)."
    )
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument(
        "--mode", choices=("update", "separate", "replace"),
        help="How to handle files that already contain another method",
    )
    args = parser.parse_args()
    target = args.project.resolve()
    if not target.is_dir():
        parser.error("The target project directory must already exist.")
    if target == SOURCE:
        parser.error("Run this command from the project adopting the method.")
    for directory in (target / ".ai", target / "prompts"):
        if directory.is_symlink():
            print(f"Cannot inspect symlinked project directory: {directory}", file=sys.stderr)
            return 1

    sources = sorted(
        p for directory in (".ai", "prompts")
        for p in (SOURCE / directory).rglob("*") if p.is_file()
    )
    if not sources or not (SOURCE / "AGENTS.md").is_file():
        parser.error("The method source is incomplete.")
    conflicts = [
        p.relative_to(SOURCE) for p in sources
        if (target / p.relative_to(SOURCE)).is_symlink()
        or ((target / p.relative_to(SOURCE)).exists()
            and (not (target / p.relative_to(SOURCE)).is_file()
                 or (target / p.relative_to(SOURCE)).read_bytes() != p.read_bytes()))
    ]
    mode = choose_mode(conflicts, args)
    if mode is None:
        return 0 if args.dry_run else 2
    separate = mode == "separate"
    if mode == "update":
        existing_method = target / ".ai/METHOD.md"
        if not existing_method.is_file() or "AI-Assisted" not in existing_method.read_text(
            encoding="utf-8", errors="replace"
        ):
            print(
                "Update requires an existing AI-Assisted method. Choose --mode separate "
                "or --mode replace instead.", file=sys.stderr
            )
            return 2

    directories = [target / ".ai"]
    if separate:
        directories += [target / NAMESPACE, target / NAMESPACE / "workflows",
                        target / NAMESPACE / "prompts"]
    else:
        directories += [target / ".ai/workflows", target / "prompts"]
    if mode in ("update", "replace"):
        directories.append(target / ".ai/ai-assisted-method-backups")
    errors = [
        f"Cannot use directory: {p}" for p in directories
        if p.is_symlink() or (p.exists() and not p.is_dir())
    ]
    if mode in ("update", "replace"):
        ignore = target / ".ai/ai-assisted-method-backups/.gitignore"
        if ignore.is_symlink():
            errors.append(f"Unsafe backup ignore file: {ignore}")
    actions = []
    preserved = []
    for source in sources:
        relative = source.relative_to(SOURCE)
        destination = target / destination_for(relative, separate)
        if target not in destination.resolve().parents or destination.is_symlink():
            errors.append(f"Unsafe destination: {destination}")
            continue
        incoming = incoming_bytes(source, separate)
        if not destination.exists():
            actions.append(("copy", relative, destination, incoming))
        elif not destination.is_file():
            errors.append(f"Not a file: {destination}")
        elif destination.read_bytes() == incoming:
            continue
        elif separate or (mode == "update" and relative in PROJECT_FILES):
            preserved.append(destination)
        elif mode in ("update", "replace"):
            actions.append(("replace", relative, destination, incoming))
        else:
            errors.append(f"Unexpected conflict: {destination}")

    agents = target / "AGENTS.md"
    if agents.is_symlink() or (agents.exists() and not agents.is_file()):
        errors.append(f"Cannot edit AGENTS.md: {agents}")
    else:
        current = agents.read_bytes() if agents.exists() else None
        try:
            if current is not None:
                current.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"AGENTS.md is not UTF-8: {agents}")
        else:
            changed, warning = agent_change(current, separate)
            if warning:
                preserved.append(agents)
                print(warning)
            if changed is not None:
                actions.append(("copy" if current is None else "edit", Path("AGENTS.md"), agents, changed))
    if errors:
        print("Installation stopped; no project files were changed:", file=sys.stderr)
        for error in errors[:10]:
            print(f"  {error}", file=sys.stderr)
        return 1

    print(f"Mode: {mode}. Planned changes: {len(actions)}.")
    if args.dry_run:
        for operation, _, destination, _ in actions:
            print(f"  {operation}: {destination.relative_to(target)}")
    if preserved:
        print(f"Preserved {len(preserved)} existing files with local changes.")
    if args.dry_run:
        return 0

    backups = [
        (relative, destination) for operation, relative, destination, _ in actions
        if destination.exists() and mode in ("update", "replace")
    ]
    if backups:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup = target / ".ai/ai-assisted-method-backups" / stamp
        counter = 1
        while backup.exists() or backup.is_symlink():
            backup = target / ".ai/ai-assisted-method-backups" / f"{stamp}-{counter}"
            counter += 1
        backup.mkdir(parents=True)
        ignore = target / ".ai/ai-assisted-method-backups/.gitignore"
        if not ignore.exists():
            ignore.write_text("*\n!.gitignore\n", encoding="utf-8")
        for relative, destination in backups:
            saved = backup / relative
            saved.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(destination, saved)
        print(f"Backed up replaced files to {backup.relative_to(target)}.")

    for _, _, destination, incoming in actions:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(incoming)
    prompt = destination_for(Path("prompts/bootstrap-new-project.md"), separate)
    print(f"Installed method in {target}. Existing project rules were preserved where specified.")
    print(f"Next: ask your coding agent to apply {prompt.as_posix()}.")
    if separate:
        print("Compare both methods before treating the staged copy as authoritative.")
    elif mode in ("update", "replace"):
        print("Review changed security rules and project settings before using the method.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
