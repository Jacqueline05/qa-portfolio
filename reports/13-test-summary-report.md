# 13 — Test Summary Report

**Release:** ShopEasy 2.4.0  
**Test window:** 2026-08-10 to 2026-08-14  
**Environment:** QA  
**Recommendation:** No-go until critical duplicate-order risk is resolved

## Results

| Metric | Result |
|---|---:|
| Planned cases | 86 |
| Executed | 86 |
| Passed | 78 |
| Failed | 8 |
| Blocked | 0 |
| Pass rate | 90.7% |

## Defect summary

- 1 Critical: duplicate order after refresh
- 1 High: stale coupon discount
- 2 Medium: layout and messaging issues

## Assessment

Core browsing works, but payment reliability is not acceptable for release. Re-run checkout smoke, API idempotency, pricing regression, and accessibility checks after fixes.
