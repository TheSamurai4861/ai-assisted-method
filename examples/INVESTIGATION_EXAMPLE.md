# Illustrative INVESTIGATION: a job appears to run twice

This is a fictional diagnostic example. No logs were inspected and no cause is asserted as fact.

## INTENT, CLASSIFY, RISK

Find why a daily import sometimes creates two completion records. Type: `INVESTIGATION`. Risk: initially `M`, because the behavior spans scheduling and persistence. Raise it to `H` if evidence points to production data integrity or a corrective migration.

## UNDERSTAND and diagnostic plan

Map the scheduler, worker retry policy, idempotency behavior, and completion-record write. Keep the first phase read-only. Plausible hypotheses include two scheduler triggers, a retry after a timeout, or one execution writing twice. Distinguish them with trigger IDs, attempt IDs, timestamps, and database write traces, using access permitted by the project security policy.

## Expected evidence

Record confirmed observations separately from hypotheses. For each hypothesis, state which log or trace would support or reject it, and what data is unavailable. Do not change the worker or add a speculative deduplication rule merely because duplicates are visible.

## REVIEW and human checkpoint

Present the best-supported diagnosis, rejected alternatives, and remaining uncertainty. Propose corrective options and their verification as a **separate** task. Human direction is needed if the investigation requires production access, changes scope, or reaches a consequential data-repair choice. Human acceptance of the diagnostic report closes this investigation; it does not imply acceptance of a fix.
