# 06 — Exploratory Testing Charter

## Charter

Explore checkout recovery paths to discover defects that scripted tests may miss.

**Timebox:** 60 minutes  
**Tester:** QA analyst  
**Build:** `checkout-2.4.0-rc1`  
**Mission:** Vary network conditions, browser navigation, and user input around payment submission.

## Heuristics

- Double-click and submit using Enter
- Refresh, back, and forward after payment
- Use slow network and interrupt requests
- Paste spaces, Unicode, long strings, and malformed card data
- Change quantity in another browser tab

## Notes and observations

- Confirmation loaded correctly after a slow response.
- Back navigation exposed a stale cart total.
- Pressing Enter twice sent two POST requests in one session.

## Follow-up

Create a high-priority defect for duplicate submission and add an idempotency check to the regression suite.
