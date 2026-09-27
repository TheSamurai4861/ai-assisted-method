# BUGFIX Workflow

> Extends `.ai/METHOD.md`. Only rules specific to correcting known incorrect behavior are defined here.

## Before BUILD

When reasonably possible:

1. reproduce the defect;
2. record the observed incorrect behavior;
3. define the expected behavior;
4. formulate a root-cause hypothesis;
5. add or identify a test that demonstrates the defect;
6. confirm that the test fails for the intended reason.

If reproduction is not possible, document the limitation and the evidence available.

Do not implement a fix before there is sufficient confidence about the failure being addressed.

Prefer correcting the underlying cause over masking the visible symptom.

## Expected evidence

Provide evidence that:

- the defect was reproduced or otherwise demonstrated;
- the regression test represents the actual defect;
- the test failed before the fix when practical;
- the fix causes the relevant test to pass;
- relevant regression tests still pass;
- the correction addresses the identified cause rather than only suppressing symptoms.
