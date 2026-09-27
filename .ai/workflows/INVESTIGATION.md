# INVESTIGATION Workflow

> Extends `.ai/METHOD.md`. Only rules specific to uncertain or unexplained behavior are defined here.

## Before BUILD

The initial phase is diagnostic only.

Do not modify production behavior while establishing the diagnosis.

Collect:

- confirmed observations;
- relevant logs, traces, measurements, or runtime behavior;
- missing information;
- one or more plausible hypotheses.

For each meaningful hypothesis, identify evidence that would support or reject it.

Use non-destructive instrumentation or diagnostic commands where possible.

Eliminate hypotheses using evidence rather than preference.

A code change may only be proposed once the diagnosis is sufficiently supported.

## Expected evidence

Provide:

- confirmed observations;
- hypotheses considered;
- evidence collected;
- hypotheses rejected and why;
- the best-supported diagnosis;
- remaining uncertainty;
- proposed corrective options, if any, clearly separated from the diagnostic findings.
