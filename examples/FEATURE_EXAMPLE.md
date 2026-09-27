# Illustrative FEATURE: weekly notification digest

This is a fictional example. It describes decisions and evidence a team would need; it does not claim an implementation or test run in this repository.

## INTENT, CLASSIFY, RISK

Let users receive one weekly summary instead of separate routine notifications. Type: `FEATURE`. Risk: `M`: it changes user-visible behavior, preferences, and a scheduled delivery path.

## UNDERSTAND and human decision

Inspect current notification categories, user preferences, delivery jobs, and unsubscribe behavior. Two product choices matter: enable the digest by default for existing users, or leave it off until they opt in. The agent presents reach and surprise trade-offs. In this illustration, the human product owner chooses **opt in** and keeps urgent notifications immediate. That choice belongs in the task contract; the agent can then implement it without repeated approval for ordinary steps.

## SPEC: acceptance criteria

- A user can enable or disable the weekly digest, and the choice persists.
- Routine eligible events appear once in the next digest; urgent events continue immediately.
- Users with no eligible events receive no empty digest.
- Existing users stay opted out unless they choose otherwise.
- Delivery failures remain observable and do not silently lose events.

## PLAN and BUILD concept

1. Add the preference and a narrow eligibility rule, with tests for existing users.
2. Build one digest for a controlled user cohort, then connect scheduling.
3. Keep the existing immediate path for urgent events and verify duplicate handling.
4. If delivery or retention assumptions fail, return to PLAN or SPEC before broadening scope.

## VERIFY, REVIEW, ACCEPT

Evidence to collect: preference persistence checks, digest composition and duplicate tests, failure-path checks, a controlled end-to-end delivery observation, and regressions for urgent notifications. Review checks the product choice, user impact, schedule boundaries, and evidence. The human owner accepts the behavior and any remaining delivery risk.
