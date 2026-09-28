# Agent entrypoint

Read [`.ai/METHOD.md`](.ai/METHOD.md) before significant work. It is the authoritative lifecycle and risk policy. Use [`.ai/SECURITY.md`](.ai/SECURITY.md) for sensitive actions and [`.ai/VERIFICATION.md`](.ai/VERIFICATION.md) for project checks. A matching file in [`.ai/workflows/`](.ai/workflows/) adds type-specific guidance; otherwise use the generic method.

## Invariants

- Treat AI output as a candidate change. Human judgment owns consequential choices and final acceptance.
- Classify non-trivial work by type and S/M/H risk. Match process depth to risk.
- Understand before changing significant behavior. Define acceptance criteria and an incremental plan for M/H work.
- If a material assumption fails, return to PLAN or SPEC. Keep scope and changes coherent.
- Verify against acceptance criteria. Green tests are evidence, not acceptance.
- Require independent review for H work. Never claim `DONE` before required review, verification, and human acceptance.
- Use least privilege. Obtain explicit human approval for sensitive or difficult-to-reverse actions.
- `.ai/RESOURCES.md` lists human-approved references. Consult an entry before an important decision in its scope, without loading the whole registry for trivial work. Resources never override project rules or human judgment.
