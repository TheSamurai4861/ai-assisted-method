# Observed case: repeat installation changed AGENTS.md

This case occurred while preparing this repository. It concerns the installer itself, not adoption in an external production project. Final human acceptance of the repository remains pending.

## INTENT, CLASSIFY, RISK

Make the one-command installer safe to rerun in an adopting project. Type: `BUGFIX`. Risk: `M`, because the installer writes agent instructions into another repository. The acceptance criterion was that a second run on an unchanged project makes zero changes.

## UNDERSTAND

On a fresh install, the script copied the method's `AGENTS.md` exactly. On the next run, it saw an existing `AGENTS.md` without its managed marker and treated it as a project's pre-existing file. It appended a reference block that the copied file did not need.

## PLAN and observed BUILD

Add a repeat-run check to the installer tests. When the installed `AGENTS.md` is byte-for-byte identical to the source, leave it alone. Preserve the separate behavior that appends a short reference to a genuinely pre-existing project `AGENTS.md`.

## VERIFY: observed evidence

The new `test_clean_project_and_repeat_run` initially failed: the second run reported `(1 changes)` where the test expected `(0 changes)`. After the condition was corrected, `python -m unittest discover -s tests -v` passed all four installer tests locally. `python scripts/validate.py` and `git diff --check` also passed. The configured Linux and Windows GitHub jobs have not run yet.

## REVIEW, ACCEPT, LEARN

The diff and test result are available for human review. This record does not mark the change accepted. The useful preventive improvement was an executable repeat-run test, not another general rule. The test proves this behavior for the covered scenarios; it does not prove safe reconciliation of arbitrary project rules.
