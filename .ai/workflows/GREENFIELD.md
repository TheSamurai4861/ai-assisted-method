# GREENFIELD Workflow

> Extends `.ai/METHOD.md`. Only rules specific to new projects or major new subsystems are defined here.

## Before BUILD

Clarify:

- product or system vision;
- intended users or consumers;
- problem being solved;
- important constraints;
- MVP scope;
- explicit non-goals;
- important decisions that would be expensive to reverse.

Prefer the **smallest architecture sufficient for the current requirements**.

When appropriate, define a first small **functional vertical slice** that exercises the essential path end to end.

Do not create abstractions, layers, services, or infrastructure solely for hypothetical future needs.

Architecture should evolve from observed requirements, constraints, and evidence.

## Expected evidence

Before accepting the initial implementation, provide evidence that:

- the MVP intent is satisfied;
- the first meaningful user/system flow works;
- important constraints are respected;
- the chosen architecture is sufficient for the current scope;
- unnecessary infrastructure has not been introduced;
- the project can be built and verified using documented commands.
