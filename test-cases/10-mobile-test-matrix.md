# 10 — Mobile Test Matrix

| Device/browser | Viewport | Priority | Coverage |
|---|---:|---:|---|
| iPhone 13 / Safari | 390×844 | P0 | Login, search, cart, checkout |
| iPhone SE / Safari | 375×667 | P1 | Checkout and keyboard behavior |
| Pixel 7 / Chrome | 412×915 | P0 | Login, catalog, checkout |
| Samsung A52 / Chrome | 360×800 | P1 | Catalog and responsive layout |
| iPad / Safari | 768×1024 | P1 | Catalog, cart, checkout |

## Mobile-specific checks

- [ ] Tap targets are large enough and do not overlap
- [ ] Sticky checkout controls do not cover form errors
- [ ] Numeric keyboard appears for postal code and card fields
- [ ] Orientation change preserves cart and entered data safely
- [ ] Slow mobile network shows progress and retry states
- [ ] No horizontal scrolling at supported widths
