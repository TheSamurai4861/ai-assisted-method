# MIGRATION Workflow

> Extends `.ai/METHOD.md`. Only rules specific to migrations are defined here.

## Before BUILD

Document:

- the current source contract, format, schema, API, or technology;
- the target contract, format, schema, API, or technology;
- incompatibilities;
- affected users, systems, data, and integrations;
- transition constraints.

Define:

- a migration strategy;
- temporary compatibility mechanisms if required;
- incremental migration stages;
- rollback or recovery strategy;
- stop conditions;
- validation before, during, and after migration.

For data migrations, consider backup, dry-run, idempotence, integrity validation, and interruption recovery where applicable.

## Expected evidence

Provide evidence that:

- compatibility assumptions were tested;
- the target contract works as intended;
- migrated data or behavior is valid;
- rollback or recovery is feasible where required;
- intermediate states are understood;
- relevant verification passes before final cutover.

No destructive or irreversible migration step may run without explicit human approval.
