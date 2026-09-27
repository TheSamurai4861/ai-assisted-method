# REFACTOR Workflow

> Extends `.ai/METHOD.md`. Only rules specific to structural change are defined here.

## Before BUILD

Map the relevant current system:

- current behavior;
- responsibilities;
- dependencies;
- public and important internal contracts;
- data/control flow;
- side effects;
- existing tests.

Identify the behavior and contracts that must remain invariant.

Add characterization tests when existing tests do not sufficiently protect important current behavior.

Define the target architecture and the concrete problems it is intended to solve.

Decompose the refactor into small, independently verifiable, and reasonably reversible steps.

The repository should remain functional after each step whenever practical.

Do not remove the old path before the replacement has been sufficiently validated.

## Expected evidence

For each step, provide evidence that:

- preserved behavior remains valid;
- relevant contracts remain intact or were intentionally changed;
- project verification passes;
- the step stayed within its intended scope.

At completion, perform a holistic architecture review confirming that:

- the target structure was actually achieved;
- complexity was reduced or intentionally relocated;
- no obsolete implementation remains unintentionally;
- new coupling or technical debt has been identified.
