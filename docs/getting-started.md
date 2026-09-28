# Getting started with the AI-Assisted Engineering Method

[Français](getting-started.fr.md) · [Project overview](../README.md) · [Authoritative method](../.ai/METHOD.md)

This guide takes you from installation to your first reviewed change. You can use the method with any coding agent that reads repository instructions. You do not need to adopt every template on day one.

> **The idea:** let the agent inspect, propose, implement, and verify quickly. You still choose consequential directions, accept meaningful risks, and decide when work is done.

## 1. Install in your project

Open a terminal **in the root of the project that will use the method**. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) for the one-command installer. The package requires Python 3.10 or newer; `uv` can use an installed or managed interpreter.

```sh
uvx --from "git+https://github.com/TheSamurai4861/ai-assisted-method.git" ai-assisted-method
```

While the Project Resources changes are only on the `feature/project-resources` branch, try this guide's version with:

```sh
uvx --from "git+https://github.com/TheSamurai4861/ai-assisted-method.git@feature/project-resources" ai-assisted-method
```

To preview a specific installation mode without changing files, add `--dry-run` and the mode. If files differ, the interactive installer offers **Update**, **Separate**, **Replace**, or **Cancel**. In a non-interactive shell, pass `--mode` explicitly.

| Situation | Command suffix | What happens |
|---|---|---|
| New project, no conflicts | none | Installs `AGENTS.md`, `.ai/`, and `prompts/` |
| Existing AI-Assisted method | `--mode update` | Backs up and updates method rules; keeps your `PROJECT_MAP.md`, `VERIFICATION.md`, and `RESOURCES.md` |
| Another method or uncertain conflicts | `--mode separate` | Places a comparison copy in `.ai/ai-assisted-method/`; keeps the existing files |
| Intentional reset | `--mode replace` | Backs up and replaces matching method files, including project templates |

For example, preview an update:

```sh
uvx --from "git+https://github.com/TheSamurai4861/ai-assisted-method.git" ai-assisted-method --mode update --dry-run
```

The installer preserves instructions outside its managed block in an existing `AGENTS.md`. It does not merge conflicting rules automatically. Update and Replace backups live under `.ai/ai-assisted-method-backups/` and are ignored by Git inside that directory. Review changed security rules and project settings before relying on them.

If you do not use `uv`, clone this repository and run `python /path/to/ai-assisted-method/scripts/install.py` from your project's root. Pass the same `--mode` and `--dry-run` options when needed.

## 2. Connect the method to your real project

Installation adds a reusable method, not knowledge of your codebase. Give your agent [`prompts/bootstrap-new-project.md`](../prompts/bootstrap-new-project.md), or say:

> Read `AGENTS.md` and `prompts/bootstrap-new-project.md`. Inspect this repository, then fill in the observed project map and real verification commands. Preserve existing project rules. Do not change product code.

Review two files with the agent:

- [`.ai/PROJECT_MAP.md`](../.ai/PROJECT_MAP.md) should describe the **observed current state**: stack, entry points, important boundaries, and confirmed constraints. Unknowns should stay marked as unknown.
- [`.ai/VERIFICATION.md`](../.ai/VERIFICATION.md) should contain commands that actually work here. Run them once. A copied template is not evidence that the checks exist.

The [resource registry](../.ai/RESOURCES.md) starts empty. Bootstrap must not invent references or add them without your approval.

## 3. Start a real task

Describe the outcome in ordinary language, then point the agent to [`prompts/start-task.md`](../prompts/start-task.md). For example:

> Use `prompts/start-task.md`. Fix the invoice total when a discount is applied twice. Keep the public API stable. Show the failing case, then verify the correction.

The agent first identifies the **intent**, task type, and S/M/H risk. It inspects current behavior before significant changes. For medium or high risk, it writes concise acceptance criteria and a plan using [`.ai/TASK_TEMPLATE.md`](../.ai/TASK_TEMPLATE.md). When direction is clear and the steps are reversible, it can continue without asking you to approve every edit.

| Risk | Typical treatment | Your role |
|---|---|---|
| **S**: local and easy to reverse | Understand, change, verify | Check the result |
| **M**: meaningful behavior or several components | Acceptance criteria, plan, verification, review | Decide material product or design trade-offs and accept the result |
| **H**: security, data, architecture, or hard-to-reverse impact | Incremental plan, stronger evidence, independent review | Approve sensitive actions and explicitly accept residual risk |

Risk follows the **impact of being wrong**, not the number of lines changed. The [method](../.ai/METHOD.md) is authoritative when you need the precise lifecycle.

## 4. Review the result

Ask for a short account of what changed, why, which acceptance criteria were met, and what evidence supports each claim. Run or inspect the relevant checks. Green tests help; they do not automatically prove the product decision is right.

If an important assumption fails, send the agent back to `PLAN` or `SPEC`. If the result raises a consequential choice, make that choice yourself. Only you give final acceptance.

The [illustrative feature example](../examples/FEATURE_EXAMPLE.md) shows a medium-risk task from intent through human acceptance. The [maintenance example](../examples/MAINTENANCE_EXAMPLE.md) shows how little process a small task needs.

## 5. Use approved project resources when useful

You can ask: **“What resources would be useful for this project?”** The agent can follow [`prompts/resource-discovery.md`](../prompts/resource-discovery.md): inspect the actual stack, identify gaps, research and compare authoritative sources when online, and propose a short list. It updates `.ai/RESOURCES.md` **only after you approve specific entries**.

Approved references are consulted when their scope matters to a task. They do not replace your decisions, project rules, observed constraints, or current official documentation. Keep the list small and remove stale entries with explicit approval. Do not copy protected books or substantial external material into the repository without the necessary rights.

## Common situations

### The project already has agent rules

Keep them. The installer preserves existing `AGENTS.md` content outside its own managed block and does not edit other agent instruction files. During bootstrap, ask the agent to identify material conflicts. Resolve those conflicts before treating one rule set as authoritative.

### Installation reports different files

Choose a mode based on what those files mean to the project. Use **Update** for an earlier AI-Assisted installation whose project map, verification commands, and approved resources you want to retain. Use **Separate** to compare two methods without displacing either. Use **Replace** only when you intend to reset the method's matching files; inspect the backup afterward. An invalid or cancelled choice makes no changes.

### I installed a separate copy

Start with `.ai/ai-assisted-method/prompts/bootstrap-new-project.md`. The staged method does not become authoritative merely because it was installed. Compare it with existing project rules and decide how they should coexist before applying it to development work.

### There is no specialized workflow for my task

Use [`prompts/start-task.md`](../prompts/start-task.md) and the generic method. Dedicated workflows exist only where the task needs distinct evidence or preconditions; no file is required for every task type.

### The agent keeps asking for approval

Clarify the desired outcome, boundaries, and acceptance criteria. The agent may execute clear, bounded, reversible, verifiable steps without interrupting you. It should still surface meaningful product choices and request approval for sensitive or difficult-to-reverse actions under [`.ai/SECURITY.md`](../.ai/SECURITY.md).

### A check fails, or tests pass but I am not convinced

Keep failures visible and investigate them. Compare verification evidence with the acceptance criteria and real user behavior. Passing tests are evidence, not final acceptance. Do not disable a check just to obtain a green result.

### There is no Internet access

The core method and installer can work from a local clone. Resource discovery should state its limitation and never invent sources. A resource can be proposed later when its source can be verified.

## Where to go next

- [`AGENTS.md`](../AGENTS.md): short entrypoint for agents.
- [`.ai/METHOD.md`](../.ai/METHOD.md): authoritative lifecycle and decision ownership.
- [`.ai/SECURITY.md`](../.ai/SECURITY.md): sensitive actions and required approval.
- [`prompts/`](../prompts/): reusable task starters.
- [`examples/`](../examples/): illustrative tasks at different risk levels.

Start with one real task. Keep the rules and checks that help; use `LEARN` to improve the method from observed failures rather than accumulating process.
