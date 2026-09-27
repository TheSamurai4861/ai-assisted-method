# Independent Review Template

An independent review assumes that a change can look correct, pass tests, and still contain defects.

The reviewer must evaluate the change independently from the Builder's conclusions.

## Review procedure

Before making any modification:

1. Read the task/specification and its acceptance criteria.
2. Read the repository rules, including `AGENTS.md` and `.ai/METHOD.md`.
3. Examine the complete relevant diff.
4. Treat the Builder's explanations and conclusions as claims to verify, not facts.
5. Complete the initial review before changing any code.

## Review axes

Evaluate the change against the following areas where relevant:

- alignment with the task intent;
- satisfaction of acceptance criteria;
- out-of-scope changes;
- logic errors;
- possible regressions;
- edge cases;
- error handling;
- quality of contracts and interfaces;
- unnecessary complexity;
- consistency with the existing architecture;
- technical debt introduced;
- quality, relevance, and coverage of tests;
- security;
- dependencies;
- performance, when relevant;
- compatibility or migration concerns, when relevant;
- observability, when relevant.

Do not require every axis to produce a finding. Focus on material issues.

## Finding format

For each finding, record:

### [SEVERITY] Short title

- **Type:** FACT / RISK / SUGGESTION
- **Blocking:** YES / NO
- **Evidence:** Concrete code, behavior, missing proof, or relevant context.
- **Why it matters:** Impact on correctness, maintainability, security, compatibility, or task intent.
- **Recommended action:** Minimal action needed to resolve or investigate the finding.

Allowed severity levels:

- `CRITICAL` — unacceptable risk or correctness/security failure requiring resolution before acceptance.
- `HIGH` — serious defect or likely regression requiring resolution before acceptance.
- `MEDIUM` — meaningful issue that should normally be corrected before acceptance.
- `LOW` — minor issue with limited impact.
- `NOTE` — observation, clarification, or non-blocking suggestion.

## Review summary

### Blocking findings
List unresolved findings that block acceptance.

### Non-blocking findings
List relevant findings that do not block acceptance.

### Missing evidence
Identify claims or acceptance criteria that are not sufficiently demonstrated.

### Areas requiring human judgment
Identify product, architectural, risk, or trade-off decisions that should not be delegated to the AI reviewer.

## Reviewer constraints

- Do not assume passing tests prove overall correctness.
- Do not approve a change solely because automated checks are green.
- Do not expand the task scope without identifying the expansion explicitly.
- Distinguish observed facts from inferred risks and optional suggestions.
- Clearly identify every finding that blocks acceptance.
- Do not modify the implementation until the initial review is complete.

## Human responsibility

An AI reviewer provides an additional validation layer. It does not replace final human review, judgment, or acceptance.
