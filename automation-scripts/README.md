# Automation sample

These samples show how I would automate a high-value checkout path with Playwright, using both Python/pytest and TypeScript styles.

The example is intentionally framework-focused and does not include a live application or credentials. It demonstrates:

- API-backed test data setup instead of UI setup
- Accessible, user-facing locators
- Assertions on the customer-visible result
- A critical-path test that belongs in a smoke suite
- Regression coverage for refresh and duplicate-order behavior

To run a version of this test in a real project, configure `baseURL`, test credentials, and a safe payment-provider test environment.
