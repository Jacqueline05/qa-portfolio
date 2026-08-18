# 07 — API Test Plan

## Endpoints

| Endpoint | Purpose |
|---|---|
| `GET /products` | Search and filter catalog |
| `POST /cart/items` | Add an item to the cart |
| `POST /orders` | Create an order |
| `GET /orders/{id}` | Retrieve order details |

## Coverage

- Verify authentication and authorization rules
- Validate required fields, types, limits, and enum values
- Confirm correct status codes and consistent error format
- Compare calculated totals with line items, tax, shipping, and discount
- Verify unavailable products cannot be ordered
- Verify repeated order requests are idempotent
- Validate response schema and sensitive-field handling

## Entry and exit

Use seeded products, users, and payment stubs in the QA environment. Exit when all P0/P1 API tests pass, schemas are validated, and no sensitive payment data appears in responses or logs.
