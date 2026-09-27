# Illustrative BUGFIX: duplicate charge on retry

This is a fictional example of a task record, not a production incident or benchmark. The evidence below describes what a team would need to collect; it is not a claim that checks were run in this repository.

## INTENT, CLASSIFY, RISK

Prevent a checkout retry from creating a second charge for the same order. Type: `BUGFIX`. Risk: `H`, because payment state and persistent records are affected. Human direction confirms that one completed order may have one captured charge; the team must also decide how to handle existing duplicates.

## UNDERSTAND

The illustrative service receives a checkout request, creates a payment attempt, calls a provider, and stores the outcome. A client timeout can trigger a retry before the first provider response is recorded. Inspect the request handler, payment record uniqueness rules, provider idempotency contract, and existing tests. Confirm actual provider behavior before relying on it.

## SPEC: acceptance criteria

- Two requests for the same order and operation produce at most one captured charge.
- A retry returns the existing outcome or a clear pending state; it does not silently create a new attempt.
- Distinct orders remain independent.
- A provider error can be retried according to an explicitly chosen policy.
- Relevant audit records contain no secrets or full payment details.

## PLAN and BUILD concept

1. Reproduce the race in a controlled test with a delayed provider response.
2. Agree on the retry and recovery policy with the human owner. Define a stable idempotency key and database constraint appropriate to the actual provider and schema.
3. Implement the smallest change that closes the race; keep any data repair as a separate approved action.
4. Verify each step. If the provider contract or database assumption fails, return to PLAN or SPEC.

## VERIFY: evidence to collect

Record the failing race test before the fix, then its result after the fix. Run payment integration tests, relevant full checks, and a manual review of provider calls and persistence transitions. Test concurrent requests, timeouts, provider errors, and distinct orders. A green test suite alone does not establish that real provider behavior matches the mock.

## REVIEW and ACCEPT

An independent reviewer checks the diff, provider assumptions, concurrency behavior, recovery path, security, and evidence. The human owner chooses the retry policy, accepts any residual risk, and gives final acceptance only after findings and verification gaps are resolved or explicitly accepted.
