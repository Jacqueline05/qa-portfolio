# 12 — Test Data Plan

## Principles

- Use synthetic accounts and payment-provider test tokens only.
- Never store real personal, card, or authentication data in the repository.
- Reset mutable data between runs so tests remain repeatable.
- Give each test run a unique email suffix, such as `qa+run-104@example.test`.

## Data sets

| Data set | Examples | Purpose |
|---|---|---|
| Products | In stock, out of stock, zero price, long name | Catalog and boundary testing |
| Users | New, existing, locked, admin | Authentication and authorization |
| Coupons | Valid, expired, minimum spend, item-specific | Pricing rules |
| Payments | Approved, declined, timeout | Checkout recovery |
| Addresses | Domestic, international, invalid postal code | Shipping validation |

## Reset strategy

Seed products and coupons before a suite, create users through an API fixture, and delete test orders after execution unless they are required for a report.
