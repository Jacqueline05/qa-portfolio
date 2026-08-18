# 08 — API Test Cases

| ID | Request | Expected |
|---|---|---|
| API-01 | `GET /products?q=shoe` | `200`; results match the query and schema |
| API-02 | `GET /products?limit=0` | `400`; structured validation error |
| API-03 | `POST /cart/items` with valid SKU and quantity 2 | `201`; line item quantity is 2 |
| API-04 | `POST /cart/items` with unknown SKU | `404`; cart is unchanged |
| API-05 | `POST /orders` with missing address | `422`; field error identifies address |
| API-06 | `POST /orders` with approved payment stub | `201`; one order and one transaction |
| API-07 | Repeat `POST /orders` with same idempotency key | Same order response; no duplicate charge |
| API-08 | `GET /orders/{id}` as another user | `403` or `404`; no order data disclosed |
| API-09 | `GET /orders/{id}` | Monetary values use a consistent decimal format |
| API-10 | Any endpoint with expired token | `401`; response contains no private data |
