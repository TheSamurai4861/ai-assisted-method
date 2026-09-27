# AI-Assisted Engineering Method

A lightweight engineering method for using AI coding agents with high useful autonomy while preserving human judgment, verification, and final control.

## Why this exists

AI can implement software quickly. Speed without structure can distance developers from understanding, intentional design, and reliable verification. This method helps teams decide deliberately what people should own and what machines should accelerate.

## Core principle

**Human judgment, AI throughput.** AI can inspect, research, propose, implement, test, and review at speed. People own intent, product direction, consequential creative and architecture choices, risk acceptance, and final acceptance. AI-generated code is a candidate change supported by evidence, not an established truth.

## Workflow

**INTENT → CLASSIFY → RISK → UNDERSTAND → SPEC → PLAN → BUILD → VERIFY → REVIEW → ACCEPT → LEARN**

Classify the task and S/M/H risk first. The depth of SPEC, PLAN, verification, and review grows with risk. Small clear changes need a light process; M/H work needs verifiable acceptance criteria and an incremental plan. Invalidated assumptions return work to PLAN or SPEC. Human acceptance closes the task.

## Autonomy

Clear, bounded, reversible, low-impact, objectively verifiable work allows more agent autonomy. Ambiguous, subjective, architectural, security-sensitive, high-impact, destructive, or hard-to-reverse work needs more human judgment. An agent should bring consequential alternatives and trade-offs to the human, then execute the chosen direction without pausing for every ordinary step. Sensitive actions still follow [the security policy](.ai/SECURITY.md).

## Quick start

From the **project adopting the method**, use this one-command installation after this repository has been populated on GitHub. It requires [uv](https://docs.astral.sh/uv/getting-started/installation/) and Git:

```sh
uvx --from git+https://github.com/TheSamurai4861/ai-assisted-method.git ai-assisted-method
```

The tool runs in an isolated environment and does not add a dependency to the adopting project. Add `--dry-run` to preview changes. It copies `.ai/` and `prompts/` into the current directory. If `AGENTS.md` already exists, it preserves the file and appends a short method reference; other repository instructions remain untouched. It stops before changing anything if an existing method or prompt file differs. Resolve any conflicting rules or files with human judgment. You can also pass an explicit target directory as the final argument.

From a local checkout, the dependency-free alternative is `python /path/to/ai-assisted-method/scripts/install.py`. On Windows, quote the path, for example `python "C:\path\to\ai-assisted-method\scripts\install.py"`.

Then:

1. Ask your coding agent to apply [bootstrap-new-project.md](prompts/bootstrap-new-project.md). It examines existing project rules, reports conflicts, and adapts the project map and verification commands to observed facts.
2. Review its changes to [PROJECT_MAP.md](.ai/PROJECT_MAP.md) and [VERIFICATION.md](.ai/VERIFICATION.md). Resolve any consequential rule conflicts.
3. Start a task using [start-task.md](prompts/start-task.md) or the relevant [workflow](.ai/workflows/). The generic [method](.ai/METHOD.md) applies when no specialized workflow exists.
4. Record M/H criteria and evidence with [TASK_TEMPLATE.md](.ai/TASK_TEMPLATE.md). Run relevant checks, review, and obtain human acceptance.

## Repository structure

| Path | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Short agent entrypoint and invariants |
| [`.ai/METHOD.md`](.ai/METHOD.md) | Authoritative lifecycle, risk, autonomy, and acceptance rules |
| [`.ai/PROJECT_MAP.md`](.ai/PROJECT_MAP.md) | Template for observed project facts |
| [`.ai/VERIFICATION.md`](.ai/VERIFICATION.md) | Evidence policy and project check configuration |
| [`.ai/SECURITY.md`](.ai/SECURITY.md) | Sensitive-action and least-privilege rules |
| [`.ai/workflows/`](.ai/workflows/) | Specialized guidance where task type warrants it |
| [`prompts/`](prompts/) | Concise task starters that apply the method |
| [`examples/`](examples/) | Illustrative task records across S/M/H risk |
| [`scripts/validate.py`](scripts/validate.py) | Dependency-free repository checks |
| [`scripts/install.py`](scripts/install.py) | Dependency-free copy into an existing project |
| [`pyproject.toml`](pyproject.toml) | Packaging for the remote `uvx` command |
| [`.github/workflows/validate.yml`](.github/workflows/validate.yml) | Validation on GitHub for Linux and Windows |

## Examples

These are illustrative task records, not reports from production projects. They show where the agent can proceed and where human judgment is needed.

| Example | Risk | Main lesson |
|---|---|---|
| [Stale CLI example](examples/MAINTENANCE_EXAMPLE.md) | S | Make a clear, reversible edit with minimal process |
| [Weekly digest](examples/FEATURE_EXAMPLE.md) | M | Let the human choose product behavior, then implement it |
| [Duplicate job investigation](examples/INVESTIGATION_EXAMPLE.md) | M initially | Separate diagnosis from a corrective change |
| [Duplicate charge bug](examples/BUGFIX_EXAMPLE.md) | H | Verify a sensitive fix and its provider assumptions |
| [Order-status migration](examples/MIGRATION_EXAMPLE.md) | H | Stage data changes and require approval for destructive cutover |

An [observed installer case](examples/INSTALLER_CASE_STUDY.md) records a real repeat-run defect found by a test during this repository's preparation. It is separate from the fictional examples and does not claim external production use or final human acceptance.

## Try it on a real project

Start with one clear S task, one ordinary M task, and one consequential H task when a genuine H task arises. For each, keep the task criteria, decisions, verification evidence, human interruptions, and any rework. Afterward, ask which checkpoints prevented a mistake and which added no value. Use [LEARN](.ai/METHOD.md) to change the smallest relevant rule or executable check. Publish a case study only with the project's permission and real evidence; the examples above do not substitute for that trial.

For this repository, run `python scripts/validate.py` and `python -m unittest discover -s tests -v`. The same checks are configured in GitHub Actions for Linux and Windows.

## What this is not

This method does not guarantee correctness, replace engineering expertise, demand a large spec for every task, require human approval for each trivial agent action, treat green tests as complete proof, or grant autonomy where decisions cannot be safely verified.

## Status

This is an evolving method, intended to improve through observed failures and practical use. It is not a universal standard or a claim of validation across every team.

## License

The code and documentation are available under the [MIT License](LICENSE).
