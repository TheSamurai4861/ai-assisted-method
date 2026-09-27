# PERFORMANCE Workflow

> Extends `.ai/METHOD.md`. Only rules specific to performance work are defined here.

## Before BUILD

Define:

- the performance metric;
- the workload or benchmark scenario;
- the measurement protocol;
- the acceptable target or improvement criterion.

Measure a baseline before modifying the implementation.

Identify the bottleneck using evidence.

Formulate a performance hypothesis that explains why the proposed change should improve the measured bottleneck.

Avoid speculative optimization without measurement.

## Expected evidence

Provide:

- baseline measurements;
- benchmark conditions;
- identified bottleneck;
- performance hypothesis;
- post-change measurements using the same protocol;
- before/after comparison;
- functional regression results;
- relevant trade-offs in CPU, memory, latency, complexity, maintainability, or cost.

Do not claim a performance improvement without measured evidence.
