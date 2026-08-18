# 04 — Bug Reports

## BUG-001 — Checkout creates duplicate order after browser refresh

**Environment:** Chrome 126, Windows 11, staging  
**Severity/Priority:** Critical / P0  
**Steps:** Add an item, complete payment, wait for confirmation, then refresh the confirmation page.  
**Expected:** The existing order is displayed and no second order is created.  
**Actual:** A second order is created with the same item and payment amount.  
**Evidence:** Two order IDs and two payment-provider transaction IDs are visible in the test account.  
**Suspected area:** Missing idempotency key on order-submission retry.

## BUG-002 — Coupon discount remains after removing eligible item

**Environment:** Edge 126, staging  
**Severity/Priority:** High / P1  
**Steps:** Add an eligible and ineligible item, apply `SAVE10`, then remove the eligible item.  
**Expected:** Coupon is removed and the total returns to the undiscounted amount.  
**Actual:** The discount remains in the cart and checkout total.  
**Workaround:** Refresh the page.
