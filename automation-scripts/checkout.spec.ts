import { expect, test } from "@playwright/test";

test.describe("checkout smoke coverage", () => {
  test("customer can place one order for an in-stock product", async ({
    page,
    request,
  }) => {
    // API setup keeps the test focused on the customer journey.
    const product = await request.post("/test-support/products", {
      data: { stock: 5, price: 29.99 },
    });
    const { id: productId } = await product.json();

    await page.goto(`/products/${productId}`);
    await page.getByRole("button", { name: "Add to cart" }).click();
    await page.getByRole("link", { name: /cart/i }).click();
    await page.getByRole("button", { name: "Checkout" }).click();

    await page.getByLabel("Email").fill("qa.customer@example.test");
    await page.getByLabel("Address line 1").fill("10 Test Street");
    await page.getByLabel("City").fill("Testville");
    await page.getByLabel("Postal code").fill("10001");
    await page.getByLabel("Card number").fill("4242 4242 4242 4242");
    await page.getByRole("button", { name: "Place order" }).click();

    await expect(page.getByRole("heading", { name: /order confirmed/i })).toBeVisible();
    await expect(page.getByTestId("order-total")).toHaveText("$29.99");

    // A refresh must show the same order, not create a second one.
    const orderNumber = await page.getByTestId("order-number").textContent();
    await page.reload();
    await expect(page.getByTestId("order-number")).toHaveText(orderNumber ?? "");
  });
});
