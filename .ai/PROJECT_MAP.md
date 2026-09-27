# Project Map

> This document describes the **observed current state** of the repository.
> It is not a target architecture, roadmap, or duplicate of the codebase.
> Update it only when structural information materially changes.

## Purpose

Briefly describe:

- what the project is;
- who or what it serves;
- its primary responsibility.

**Current purpose:**
[TO DEFINE]

---

## Stack

Record only important technologies and versions that materially affect development.

| Area | Technology | Version / Notes |
|---|---|---|
| Language(s) | [TO DEFINE] | [TO DEFINE] |
| Framework(s) | [TO DEFINE] | [TO DEFINE] |
| Runtime(s) | [TO DEFINE] | [TO DEFINE] |
| Package / dependency management | [TO DEFINE] | [TO DEFINE] |
| Other important tooling | [TO DEFINE] | [TO DEFINE] |

---

## Repository structure

Describe only the main directories and their responsibilities.

```text
[repository-root]/
├── [directory]   # [responsibility]
├── [directory]   # [responsibility]
└── ...
```

Avoid documenting individual files unless they are structurally important.

---

## Entry points

List the main places where execution, requests, jobs, or major workflows begin.

| Entry point | Responsibility |
|---|---|
| [TO DEFINE] | [TO DEFINE] |

---

## Architecture

Summarize the major components, layers, modules, or bounded areas and their responsibilities.

Focus on:

- ownership of responsibilities;
- important boundaries;
- major dependencies;
- direction of communication.

**Observed architecture:**
[TO DEFINE]

---

## Data flow

Describe the most important data or control flows at a high level.

Example structure:

```text
[Source]
  ↓
[Component]
  ↓
[Transformation / domain logic]
  ↓
[Persistence / external system]
```

**Important flows:**
[TO DEFINE]

---

## External systems

List external systems the project depends on.

| System | Type | Purpose | Important notes |
|---|---|---|---|
| [TO DEFINE] | API / DB / service / queue / storage / other | [TO DEFINE] | [TO DEFINE] |

Do not include credentials or secrets.

---

## State and persistence

Describe:

- where application state lives;
- what is persistent versus ephemeral;
- important caches;
- databases or storage mechanisms;
- synchronization behavior if relevant.

**Observed state model:**
[TO DEFINE]

---

## Build

### Prerequisites

- [TO DEFINE]

### Main commands

```text
[TO DEFINE]
```

### Important notes

- [TO DEFINE]

---

## Tests

Describe the test layers that actually exist.

| Test type | Location / scope | Command | Notes |
|---|---|---|---|
| Unit | [TO DEFINE] | [TO DEFINE] | [TO DEFINE] |
| Integration | [TO DEFINE] | [TO DEFINE] | [TO DEFINE] |
| End-to-end | [TO DEFINE] | [TO DEFINE] | [TO DEFINE] |

Remove rows that do not apply.

---

## Static checks

Record the checks that actually exist.

| Check | Tool | Command | Notes |
|---|---|---|---|
| Formatting | [TO DEFINE] | [TO DEFINE] | [TO DEFINE] |
| Linting | [TO DEFINE] | [TO DEFINE] | [TO DEFINE] |
| Type checking | [TO DEFINE] | [TO DEFINE] | [TO DEFINE] |
| Static analysis | [TO DEFINE] | [TO DEFINE] | [TO DEFINE] |

Remove rows that do not apply.

---

## CI/CD

Summarize the real pipeline.

Include only structurally important stages such as:

- validation;
- build;
- test;
- packaging;
- deployment;
- release.

**Pipeline:**
[TO DEFINE]

**Important triggers / environments:**
[TO DEFINE]

---

## Sensitive areas

Identify parts of the system that require additional care.

Examples include:

- authentication;
- authorization;
- secrets;
- payments;
- personal or production data;
- destructive operations;
- migrations;
- deployment;
- security policy;
- externally exposed endpoints.

| Area | Why sensitive | Relevant location / boundary |
|---|---|---|
| [TO DEFINE] | [TO DEFINE] | [TO DEFINE] |

Do not place secrets in this document.

---

## Important conventions

Record only conventions that materially affect safe and consistent changes.

Examples:

- dependency direction;
- naming or module boundaries;
- where domain logic belongs;
- error-handling conventions;
- testing expectations;
- generated-code boundaries.

- [TO DEFINE]

Do not duplicate general style rules already enforced automatically.

---

## Known architectural constraints

List constraints that must not be broken accidentally.

Examples:

- backward-compatible public contract;
- offline support;
- strict layer boundary;
- database compatibility;
- platform limitation;
- latency or memory requirement.

- [TO DEFINE]

Only record constraints that are confirmed by the repository, documentation, or project stakeholders.

---

## Open questions

Record structural facts that are still unknown, ambiguous, or require confirmation.

- [TO DEFINE]

Remove questions once they are resolved and update the relevant section instead.
