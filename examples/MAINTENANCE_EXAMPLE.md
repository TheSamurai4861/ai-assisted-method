# Illustrative MAINTENANCE: correct a stale CLI example

This is a fictional example. No project command was run and no result below is presented as observed evidence.

## INTENT, CLASSIFY, RISK

A project's README shows `tool check --quick`, but the documented CLI now uses `--fast`. Correct the example so a new contributor can run it. Type: `MAINTENANCE`. Risk: `S`: the change is confined to documentation, easily reversed, and objectively checked.

## UNDERSTAND and BUILD

The agent inspects the actual CLI help and existing package scripts, confirms the supported flag, and edits only the stale command. A formal SPEC or written PLAN would add little here. If the CLI and scripts disagree, the task is no longer clear; the agent stops to investigate before editing.

## VERIFY, REVIEW, ACCEPT

Evidence to collect: the CLI's help output, a search for other uses of the old flag, and a check that the README command runs in a suitable local environment. The agent reports the exact documentation diff and any environment limitation. A lightweight human check of the result is enough for final acceptance. The agent need not request permission before this bounded edit.
