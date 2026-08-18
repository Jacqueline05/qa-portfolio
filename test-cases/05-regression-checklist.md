# 05 — Regression Checklist

## Authentication

- [ ] Valid user can sign in and sign out
- [ ] Invalid password is rejected without revealing account details
- [ ] Password reset link can be requested

## Catalog and cart

- [ ] Search, sorting, and filters return accurate results
- [ ] Product images, price, stock, and variant selection are correct
- [ ] Quantity changes update subtotal
- [ ] Removing the final item shows an empty-cart state

## Checkout

- [ ] Required fields and invalid formats are validated
- [ ] Shipping options update the total
- [ ] Valid, invalid, expired, and minimum-spend coupons behave correctly
- [ ] Approved and declined payments produce the correct result
- [ ] Refreshing or double-clicking does not duplicate an order

## Orders and release safety

- [ ] Confirmation email contains the correct order number and total
- [ ] Order history reflects the new order
- [ ] No critical console errors or failed network calls are present
