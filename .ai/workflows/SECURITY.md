# SECURITY Workflow

> Extends `.ai/METHOD.md` and `.ai/SECURITY.md`. Only rules specific to security-sensitive tasks are defined here.

## Before BUILD

Create a lightweight threat model covering:

- assets to protect;
- actors and trust levels;
- trust boundaries;
- attack surface;
- plausible abuse cases;
- sensitive data;
- required privileges.

Define explicit security requirements and the evidence required to validate them.

Apply least privilege to:

- filesystem access;
- network access;
- credentials;
- external services;
- runtime permissions;
- production access.

Treat security-sensitive decisions as high risk unless clearly demonstrated otherwise.

## Expected evidence

Provide evidence appropriate to the change, such as:

- security-focused tests;
- permission checks;
- input validation tests;
- authentication/authorization checks;
- dependency or supply-chain validation;
- static or dynamic security analysis;
- negative/abuse-case testing;
- confirmation that secrets were not exposed.

Security-sensitive changes require strengthened independent review.

Human approval is mandatory before sensitive or difficult-to-reverse security decisions or actions.
