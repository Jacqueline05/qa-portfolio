# 02 — Test Scenarios

| ID | Scenario | Expected outcome |
|---|---|---|
| TS-01 | Search by exact product name | Matching products are displayed |
| TS-02 | Search with no results | Helpful empty state is shown |
| TS-03 | Filter by category and price | Results satisfy every selected filter |
| TS-04 | Add available item to cart | Cart count and subtotal update |
| TS-05 | Add item that becomes unavailable | User receives a clear stock message |
| TS-06 | Apply valid coupon | Discount and final total are correct |
| TS-07 | Submit checkout with missing fields | Field-level validation appears |
| TS-08 | Pay with approved card | One order is created and confirmation is shown |
| TS-09 | Pay with declined card | No order is created; retry guidance appears |
| TS-10 | Refresh after payment | Order is not duplicated |
| TS-11 | View order history | Latest order has correct status and amount |
| TS-12 | Navigate checkout with keyboard only | All controls are reachable and usable |
