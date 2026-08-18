# 11 — Requirements Traceability Matrix

| Requirement | Test coverage | Defect | Status |
|---|---|---|---|
| R-01 Customer can search products | TS-01, TS-02, API-01 | — | Covered |
| R-02 Customer can add available items | TS-04, TC-CHK-001, API-03 | — | Covered |
| R-03 Checkout validates required data | TS-07, TC-CHK-002, API-05 | — | Covered |
| R-04 Approved payment creates one order | TS-08, TC-CHK-001, API-06 | BUG-001 | At risk |
| R-05 Declined payment does not create order | TS-09, TC-CHK-003, API-06 | — | Covered |
| R-06 Coupon total is accurate | TS-06, regression checklist, API-09 | BUG-002 | At risk |
| R-07 Checkout is keyboard accessible | TS-12, accessibility review | ACC-001 | At risk |

## Coverage summary

5 of 7 requirements are covered without known defects. Three areas require release decision input because open defects affect reliability, pricing, or accessibility.
