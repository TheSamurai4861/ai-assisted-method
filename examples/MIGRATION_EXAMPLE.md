# Illustrative MIGRATION: replace a legacy order-status field

This is a fictional example. The steps and evidence are a plan, not a claim that data was migrated.

## INTENT, CLASSIFY, RISK

Move order status from a free-text field to a constrained status code while keeping older clients working during rollout. Type: `MIGRATION`. Risk: `H`, because persistent data, compatibility, and a later destructive cleanup are involved.

## UNDERSTAND and human decisions

Inventory values actually stored, readers and writers, API contracts, and reporting jobs. Unknown historical values may not map cleanly. The agent proposes mappings and options for unknowns; the human owner chooses their meaning and acceptable compatibility period. No data is silently discarded or reinterpreted.

## SPEC: acceptance criteria

- Every known legacy value has a documented mapping or an explicit exception path.
- New writes use the target status while old clients still receive the agreed legacy representation during transition.
- A dry run reports unmapped and inconsistent records without changing them.
- Backfill can resume safely after interruption and preserves record counts and identity.
- Rollback or recovery remains feasible until the human-approved cutover point.

## PLAN and BUILD concept

1. Add the new field and compatible read/write behavior; verify old and new contracts.
2. Run a non-destructive inventory and dry run. Stop if unmapped values exceed the agreed policy.
3. Backfill in bounded batches with checkpoints and integrity checks.
4. Cut over readers after compatibility evidence and independent review.
5. Remove the old field only as a separate, explicitly approved destructive step.

An invalid mapping or compatibility assumption returns the work to PLAN or SPEC.

## VERIFY, REVIEW, ACCEPT

Evidence to collect: before/after value counts, mapping exceptions, dry-run results, interrupted-batch recovery, old-client compatibility checks, and relevant full verification. An independent reviewer examines the plan, diff, evidence, and recovery path. The human decides the unknown-value policy, approves any irreversible action, accepts residual risk, and gives final acceptance.
