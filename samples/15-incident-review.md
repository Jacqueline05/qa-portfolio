# 15 — Post-release Incident Review

## Incident

**Title:** Duplicate orders created when customers refreshed confirmation  
**Impact:** 14 duplicate orders over 35 minutes; customers were charged twice before manual refunds began.  
**Severity:** SEV-1  
**Detection:** Customer support report, followed by payment reconciliation alert.

## Timeline

- 09:05 — Checkout release deployed
- 09:22 — First duplicate order created
- 09:40 — Support escalated repeated customer reports
- 09:47 — Order creation disabled
- 10:15 — Refunds and customer notifications started
- 13:30 — Idempotency fix deployed and verified

## Root cause

The confirmation page retried the order request after a navigation refresh. The service did not require or persist an idempotency key, so each request created a new order and payment.

## Corrective actions

- Require an idempotency key for order creation.
- Add API and UI tests for refresh, retry, and double-click behavior.
- Add a reconciliation alert for near-identical orders.
- Add a release checklist item for payment retry paths.
- Run a targeted regression suite before re-enabling checkout.

## Learning

Happy-path payment testing was insufficient; retry and recovery behavior must be treated as a primary checkout workflow.
