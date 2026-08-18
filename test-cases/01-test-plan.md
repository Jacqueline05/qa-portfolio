# 01 — Test Plan

## Objective

Validate the ShopEasy checkout release so customers can find products, add them to a cart, pay securely, and receive an accurate order confirmation.

## Scope

**In scope:** product search, product details, cart, coupons, address entry, shipping, payment, order creation, confirmation email, and order history.

**Out of scope:** warehouse fulfillment, payment-provider internal processing, and performance benchmarking.

## Approach

- Smoke testing on every build
- Functional and negative testing for checkout
- Cross-browser testing on Chrome, Edge, and Safari
- API validation for cart, order, and payment endpoints
- Accessibility checks for keyboard navigation and form labels
- Regression testing of account and catalog features

## Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Duplicate order after refresh | High | Verify idempotency and retry behavior |
| Incorrect tax or shipping total | High | Compare UI totals with API response |
| Coupon applied incorrectly | Medium | Test expired, invalid, and boundary coupons |

## Entry and exit criteria

**Entry:** deployed build, approved requirements, stable test environment, and seeded test data.

**Exit:** all critical tests pass, no open blocker/critical defects, and residual risk is accepted by the product owner.
