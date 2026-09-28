# Bootstrap a project

Adapt this method to the current repository. Read AGENTS.md, .ai/METHOD.md, .ai/PROJECT_MAP.md, .ai/VERIFICATION.md, and .ai/SECURITY.md. Inspect the project before editing documentation.

First identify existing repository instructions, including more specific AGENTS.md files and other agent rule files such as CLAUDE.md, .github/copilot-instructions.md, or .cursor/rules/ when present. Preserve those rules. Report material conflicts with the generic method for human resolution; do not silently replace either rule set.

If another methodology remains alongside these files, compare the two explicitly. Preserve observed project facts and real verification commands. Explain any conflicting rule, its practical effect, and the smallest decision needed from the human owner before treating one rule as authoritative.

Fill .ai/PROJECT_MAP.md with observed purpose, stack and versions, structure, entry points, architecture, data flow, external systems, persistence, build and check commands, CI/CD, conventions, sensitive areas, and confirmed constraints. Configure .ai/VERIFICATION.md using commands that actually exist.

Do not change product code or propose a refactor in this task. Mark facts that cannot be established as unknown. Do not invent commands, versions, or architecture.
