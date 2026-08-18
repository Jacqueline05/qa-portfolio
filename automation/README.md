# Automation sample

This sample shows how I would automate a high-value checkout path with Playwright.

The example is intentionally framework-focused and does not include a live application or credentials. It demonstrates:

- API-backed test data setup instead of UI setup
- Accessible, user-facing locators
- Assertions on the customer-visible result
- A critical-path test that belongs in a smoke suite

To run a version of this test in a real project, configure `baseURL`, test credentials, and a safe payment-provider test environment.
