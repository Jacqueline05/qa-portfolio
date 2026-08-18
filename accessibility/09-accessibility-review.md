# 09 — Accessibility Review

**Standard:** WCAG 2.2 AA  
**Page:** Checkout  
**Method:** Keyboard review, screen-reader spot check, zoom, and contrast inspection

| Check | Result | Notes |
|---|---|---|
| Every input has an associated label | Pass | Labels match input purpose |
| Keyboard focus is visible | Pass | Focus ring remains visible |
| Focus order follows the visual order | Fail | Coupon field is skipped after tabbing |
| Errors are announced and connected to fields | Fail | Error text is not referenced by `aria-describedby` |
| Buttons have accessible names | Pass | Submit button has clear name |
| Page works at 200% zoom | Pass | No content is clipped |
| Text and controls meet contrast target | Pass | Spot checks meet 4.5:1 |
| Status updates are announced | Needs review | Confirmation message should use a live region |

## Recommendation

Fix the two failed checks before release and retest with keyboard-only navigation and a screen reader.
