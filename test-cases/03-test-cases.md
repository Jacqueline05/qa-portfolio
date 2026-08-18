# 03 — Detailed Test Cases

## TC-CHK-001 — Successful checkout

**Priority:** Critical  
**Preconditions:** A sellable product exists; test card `4242 4242 4242 4242` is available.

1. Open the product page.
2. Select a valid quantity and click **Add to cart**.
3. Open the cart and click **Checkout**.
4. Enter a valid shipping address.
5. Enter the approved test card and submit payment.

**Expected:** The payment succeeds once, an order number is generated, the cart is empty, and the confirmation page shows the correct item, shipping, tax, and total.

## TC-CHK-002 — Required field validation

**Priority:** High

1. Open checkout with an item in the cart.
2. Leave the email, address, and card fields blank.
3. Click **Place order**.

**Expected:** Each required field shows an actionable validation message; no payment request or order is created.

## TC-CHK-003 — Declined payment

**Priority:** High

1. Complete checkout using the declined-card test number.
2. Submit the order.

**Expected:** A payment-declined message is shown, the cart remains intact, and the customer can retry without duplicate orders.
