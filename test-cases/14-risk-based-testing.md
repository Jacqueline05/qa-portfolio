# 14 — Risk-Based Testing

## Risk scoring

Score each area from 1–5 for **impact** and **likelihood**. Priority is the product of both scores.

| Area | Impact | Likelihood | Score | Test priority |
|---|---:|---:|---:|---|
| Payment and order creation | 5 | 4 | 20 | Highest |
| Price, tax, and coupons | 5 | 3 | 15 | Highest |
| Authentication and access | 5 | 3 | 15 | Highest |
| Product search | 3 | 3 | 9 | Medium |
| Visual styling | 2 | 2 | 4 | Lower |

## Prioritized execution

1. Run payment smoke and duplicate-submission tests.
2. Validate totals through UI and API.
3. Verify authorization and account recovery.
4. Run core catalog and cart regression.
5. Complete visual polish and low-impact compatibility checks.

This approach concentrates limited test time on failures that could cause financial loss, data exposure, or customer-impacting orders.
