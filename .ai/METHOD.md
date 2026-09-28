# AI-Assisted Engineering Method

## 1. Core Principle

**AI-generated code is never considered correct by default.**

AI produces a **candidate change supported by evidence**.
Final acceptance remains a **human responsibility**.

The goal is **human judgment, AI throughput**: use AI's speed for analysis, implementation, and evidence, while keeping consequential decisions and final acceptance with people.

### Decision ownership

The human owns intent, problem definition, product direction, important creative and UX choices, major architecture and scope trade-offs, risk acceptance, difficult-to-reverse decisions, and final acceptance. An agent may research, inspect, challenge assumptions, propose options, implement an established direction, test, analyze failures, and review. A proposal is not a decision: when alternatives have consequential trade-offs, present them and obtain a human choice before committing to one.

### Autonomy and checkpoints

Give the agent more autonomy as work becomes **clear, bounded, reversible, low impact, and objectively verifiable**. Require more human judgment as work becomes **ambiguous, subjective, architectural, security-sensitive, high impact, destructive, or difficult to reverse**. Technical ease never reduces the controls required for a sensitive action; `.ai/SECURITY.md` applies.

Pause for human direction when intent is unclear, product or UX options materially differ, a major architecture or scope decision is needed, a meaningful risk must be accepted, or a sensitive action needs approval. Once direction is clear, continue through ordinary reversible steps without asking for approval at every phase. Present the result and evidence for human acceptance at the end.

---

## 2. General Workflow

Every non-trivial task follows this lifecycle:

**INTENT → CLASSIFY → RISK → UNDERSTAND → SPEC → PLAN → BUILD → VERIFY → REVIEW → ACCEPT → LEARN**

The depth of each phase depends on the task's complexity and risk.

### INTENT

Define why the task exists and what outcome is expected.

The intent must describe the problem or desired result, not prescribe an implementation unless that implementation is itself a constraint.

### CLASSIFY

Assign the task to the most appropriate task type:

- `GREENFIELD` — starting a new project or major isolated subsystem.
- `FEATURE` — adding or extending behavior.
- `BUGFIX` — correcting known incorrect behavior.
- `INVESTIGATION` — diagnosing uncertain or unexplained behavior.
- `REFACTOR` — changing internal structure while preserving intended behavior.
- `MIGRATION` — moving between technologies, schemas, APIs, formats, or architectures.
- `PERFORMANCE` — improving measurable performance.
- `SECURITY` — addressing security-sensitive behavior or controls.
- `HOTFIX` — urgent, narrowly scoped corrective change.
- `MAINTENANCE` — dependency, tooling, configuration, cleanup, or routine technical work.
- `SPIKE` — time-bounded technical exploration or prototype.
- `ONBOARDING` — understanding and documenting an unfamiliar codebase or subsystem.

Choose the type according to the **dominant engineering problem**, not merely the wording of the request.

If a task contains multiple concerns, use one primary type and note important secondary concerns.

The generic lifecycle applies to every type. Use a file in `.ai/workflows/` only when one exists for the chosen type; the absence of a dedicated workflow adds no extra process.

### RISK

Assign one risk level:

#### S — Small

Use when the task is:

- local;
- low impact;
- easy to understand;
- easy to verify;
- easily reversible.

Typical examples include small text changes, simple configuration edits, or isolated low-risk fixes.

#### M — Medium

Use when the task:

- changes real behavior;
- affects several files or components;
- modifies an internal contract;
- requires non-trivial reasoning;
- can introduce meaningful regressions.

This is the default level for ordinary engineering work.

#### H — High

Use when the task affects or may affect:

- architecture;
- authentication or authorization;
- security boundaries;
- persistent data;
- migrations;
- destructive operations;
- critical dependencies;
- compatibility guarantees;
- production infrastructure;
- difficult-to-reverse behavior.

When uncertain between two levels, choose the higher level until the uncertainty is resolved.

---

## 3. Process Proportional to Risk

The methodology must not create unnecessary bureaucracy.

### Risk S

Expected process:

**UNDERSTAND → BUILD → VERIFY → ACCEPT**

A formal spec or written plan is optional when the change is obvious, local, and safely reversible.

### Risk M

Expected process:

**UNDERSTAND → SPEC → PLAN → BUILD → VERIFY → REVIEW → ACCEPT**

A concise spec and implementation plan are required.

### Risk H

Expected process:

**UNDERSTAND → SPEC → EXPLICIT PLAN → INCREMENTAL BUILD → VERIFY EACH STEP → INDEPENDENT REVIEW → DEEP HUMAN ACCEPTANCE**

High-risk work must:

- be decomposed into small, reversible steps;
- preserve a valid project state whenever reasonably possible;
- define rollback or recovery considerations when relevant;
- receive independent review before final acceptance.

---

## 4. UNDERSTAND

Before modifying non-trivial code, establish sufficient understanding of the affected system.

At minimum, determine:

- current behavior;
- relevant components and boundaries;
- existing contracts;
- dependencies;
- tests and verification mechanisms;
- important constraints;
- known unknowns;
- assumptions required to proceed.

Do not modify code merely to discover what the code already explains.

For `INVESTIGATION`, diagnosis must remain separate from implementation until sufficient evidence exists.

### Project resources

During UNDERSTAND, check whether `.ai/RESOURCES.md` has an approved reference relevant to the task. Consult only relevant entries before SPEC or PLAN decisions they can inform. BUILD follows the chosen direction rather than applying a reference mechanically; VERIFY and REVIEW may use it as supporting evidence. This is not another required phase, and trivial unrelated work needs no resource lookup.

Priority when guidance conflicts: explicit human intent and decisions, project rules, observed constraints, current official technology documentation, approved resources, then generic principles. A resource is a reference, not an authority over human judgment. If an important reference may be stale, verify its currency when possible. Add, replace, or remove registry entries only with explicit human approval; use the resource-discovery prompt when asked to discover candidates.

---

## 5. SPEC

A specification is mandatory for:

- every `M` task;
- every `H` task;
- any task with ambiguous expected behavior;
- any task that changes a public or important internal contract;
- any task whose correctness cannot be judged from the implementation alone.

A specification must define, as applicable:

- current behavior;
- expected behavior;
- scope;
- non-goals;
- constraints;
- assumptions;
- acceptance criteria;
- verification strategy.

A specification should be no larger than necessary to remove meaningful ambiguity.

---

## 6. PLAN

A written plan is mandatory for:

- every `M` task;
- every `H` task;
- large refactors;
- migrations;
- security-sensitive work;
- tasks involving multiple dependent changes.

The plan must:

- identify the main implementation steps;
- keep steps as small and independently verifiable as reasonably possible;
- identify major risks;
- identify required tests or verification;
- identify dependencies between steps;
- avoid unrelated cleanup unless explicitly included in scope.

For `H` tasks, the plan must favor **incremental and reversible execution** over one large change.

### Invalidated Assumptions

If an important assumption used by the spec or plan is proven false:

**STOP → update understanding → return to PLAN**

Do not silently improvise around a broken assumption.

If the invalidated assumption changes the intended outcome, return to `SPEC` before continuing.

---

## 7. BUILD

Implementation must follow the agreed scope and plan. A written plan does not require a separate human approval when the direction is already clear and the steps are bounded and reversible. Follow the human checkpoints and security approval rules above.

Rules:

- keep changes as small as reasonably possible;
- prefer coherent changes over broad rewrites;
- avoid unrelated modifications;
- preserve existing contracts unless changing them is part of the task;
- do not introduce unnecessary abstractions;
- do not expand scope merely because additional cleanup is convenient;
- document material deviations from the plan.

For large tasks, complete and verify one meaningful slice before proceeding to the next.

---

## 8. VERIFY

Every implementation must produce evidence appropriate to the task.

Possible evidence includes:

- tests;
- static analysis;
- type checking;
- linting;
- build results;
- benchmarks;
- security checks;
- compatibility checks;
- targeted manual validation;
- inspection of resulting behavior.

Verification must correspond to the acceptance criteria.

### Tests Are Necessary Evidence, Not Final Proof

A passing test suite does **not** by itself prove that a change is correct.

Tests may be incomplete, incorrectly specified, too narrow, or unable to detect architectural and product-level regressions.

Therefore:

**GREEN TESTS ≠ AUTOMATIC ACCEPTANCE**

Verification must consider both executable evidence and the actual intent of the task.

---

## 9. REVIEW

Review depth must be proportional to risk.

### S

A lightweight human check is normally sufficient.

### M

Review should examine:

- correctness;
- scope;
- regressions;
- tests;
- maintainability;
- relevant architectural effects.

Independent AI review may be used when useful.

### H

Independent review is required.

Whenever practical, the reviewer should operate from a fresh context and evaluate:

- the task specification;
- the resulting diff;
- verification evidence;
- relevant project rules.

The reviewer must not assume the builder's conclusions are correct.

AI review complements but does not replace human judgment.

---

## 10. ACCEPT

Acceptance is a human decision.

Before accepting a significant change, the human should be able to answer:

- What changed?
- Why was this approach chosen?
- What assumptions were made?
- What could regress?
- What evidence shows the intended behavior works?
- Were the acceptance criteria satisfied?
- Are any risks or follow-up tasks unresolved?

No agent may treat its own completion statement as final acceptance.

---

## 11. Definition of Done

A task is `DONE` only when all applicable conditions are satisfied:

- intent is understood;
- required specification exists;
- required plan exists;
- implementation remains within scope;
- acceptance criteria are satisfied;
- relevant automated checks pass;
- required manual validation is complete;
- required review is complete;
- unresolved risks are documented;
- human acceptance has been given.

For high-risk work, `DONE` additionally requires independent review and appropriate recovery or rollback considerations when relevant.

---

## 12. LEARN

The methodology must improve from observed failures, not hypothetical fears.

After meaningful rework, escaped bugs, incorrect assumptions, verification gaps, security issues, or process failures, identify:

1. the symptom;
2. the root cause;
3. the smallest preventive improvement.

Possible improvements include:

- adding or improving a test;
- strengthening executable verification;
- improving project documentation;
- updating a workflow;
- refining a rule;
- reducing permissions;
- improving architecture or observability.

Do not automatically add a new written rule for every mistake.

Prefer executable safeguards when they can enforce the invariant more reliably.

---

## 13. Rule Maintenance

Rules are working engineering assets and must remain useful.

Periodically:

- remove obsolete rules;
- merge duplicated rules;
- simplify overly specific instructions;
- move project-specific knowledge out of generic methodology;
- replace textual rules with executable checks where practical;
- delete process steps that add cost without improving outcomes.

A rule that is no longer useful should be **removed**, not kept indefinitely for historical reasons.

The objective is not to accumulate process.

The objective is to maintain the smallest methodology that reliably produces understandable, verifiable, reviewable, and human-approved software changes.
