# Verification Contract

## Principle

Every claim of success must be supported by evidence appropriate to the task.

Verification exists to demonstrate that the intended outcome was achieved without introducing unacceptable regressions.

Evidence must correspond to the task's acceptance criteria.

---

## Evidence categories

Depending on the task, verification may include:

- formatting;
- linting;
- static analysis;
- type checking;
- unit tests;
- integration tests;
- end-to-end tests;
- build validation;
- benchmarks;
- targeted manual validation;
- security scans;
- compatibility checks;
- migration dry-runs;
- project-specific checks.

Not every category is required for every task.

The required evidence depends on:

- task type;
- risk level;
- affected surface;
- acceptance criteria;
- known failure modes;
- project-specific constraints.

---

## Verification levels

### FAST

Purpose: provide a short feedback loop during implementation.

`FAST` should run the smallest useful set of checks that can catch likely defects quickly.

Typical candidates may include:

- formatting checks;
- lint;
- type checking;
- targeted unit tests;
- tests for the modified component;
- lightweight static analysis.

`FAST` does not replace final validation for significant tasks.

### FULL

Purpose: validate a significant change before review or human acceptance.

`FULL` should include all checks materially relevant to the task and project.

Depending on the project, it may include:

- full formatting validation;
- lint;
- static analysis;
- type checking;
- unit tests;
- integration tests;
- end-to-end tests;
- build;
- security checks;
- compatibility validation;
- benchmarks;
- migration dry-runs;
- required targeted manual validation.

For `M` and `H` tasks, `FULL` verification is expected unless the task documents why a specific check is not applicable or unavailable.

---

## Verification rules

1. **Never hide a failure.**
   A failing check must remain visible until it is resolved, explicitly accepted, or documented as unrelated with sufficient evidence.

2. **Never disable a test merely to obtain a green result.**
   A test may only be changed or removed when its expectation is demonstrably incorrect, obsolete, or intentionally changed by the task.

3. **Do not invent missing controls.**
   If the project does not currently provide a required verification mechanism, state that limitation explicitly.

4. **Passing tests do not automatically mean the task is complete.**
   Automated tests are evidence, not final proof of correctness.

5. **Evidence must map to acceptance criteria.**
   Important criteria must have a corresponding verification method.

6. **Use the narrowest useful check during iteration and broader checks before acceptance.**

7. **Do not weaken verification to accommodate the implementation.**
   If verification exposes a real defect, fix the defect or revisit the plan.

8. **Record material gaps.**
   Missing tests, unavailable environments, inaccessible services, or unverifiable claims must be stated explicitly before acceptance.

---

## Acceptance evidence

Before a task can be considered complete, record the relevant evidence:

- commands executed;
- checks performed;
- test results;
- build results;
- benchmark results;
- security results;
- compatibility results;
- manual observations;
- known gaps or limitations.

For significant tasks, the evidence should be sufficient for an independent reviewer to understand how the result was validated.

---

# Project-specific configuration

Complete this section when initializing the methodology for a project.

## FAST verification

### Command
```text
[TO DEFINE]
```

### Includes
- [TO DEFINE]

### Excludes / known limitations
- [TO DEFINE]

---

## FULL verification

### Command
```text
[TO DEFINE]
```

### Includes
- [TO DEFINE]

### Excludes / known limitations
- [TO DEFINE]

---

## Formatting

- Tool:
- Command:
- Notes:

## Linting

- Tool:
- Command:
- Notes:

## Static analysis

- Tool:
- Command:
- Notes:

## Type checking

- Tool:
- Command:
- Notes:

## Unit tests

- Tool:
- Command:
- Notes:

## Integration tests

- Tool:
- Command:
- Notes:

## End-to-end tests

- Tool:
- Command:
- Notes:

## Build

- Tool:
- Command:
- Notes:

## Benchmarks

- Tool:
- Command:
- Notes:

## Targeted manual validation

- Procedure:
- Notes:

## Security checks

- Tool:
- Command:
- Notes:

## Compatibility checks

- Tool:
- Command:
- Notes:

## Migration dry-run

- Tool / procedure:
- Command:
- Notes:

## Other project-specific checks

- Check:
- Command / procedure:
- Notes:
