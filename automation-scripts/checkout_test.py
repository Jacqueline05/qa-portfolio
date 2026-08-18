"""Illustrative pytest + Playwright checkout smoke test.

The endpoint and selectors are fictional portfolio examples. A real project
would provide the base URL, test data fixture, and payment sandbox settings.
"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_customer_can_place_one_order(page: Page) -> None:
    page.goto("/products/SKU-TEST-001")
    page.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name=re.compile("cart", re.IGNORECASE)).click()
    page.get_by_role("button", name="Checkout").click()

    page.get_by_label("Email").fill("qa.customer@example.test")
    page.get_by_label("Address line 1").fill("10 Test Street")
    page.get_by_label("City").fill("Testville")
    page.get_by_label("Postal code").fill("10001")
    page.get_by_label("Card number").fill("4242 4242 4242 4242")
    page.get_by_role("button", name="Place order").click()

    expect(page.get_by_role("heading", name=re.compile("order confirmed", re.IGNORECASE))).to_be_visible()
    expect(page.get_by_test_id("order-total")).to_have_text("$29.99")


@pytest.mark.regression
def test_refresh_does_not_duplicate_order(page: Page) -> None:
    # In a real suite, an API fixture would create the order and return its ID.
    page.goto("/orders/ORDER-TEST-001")
    order_number = page.get_by_test_id("order-number").inner_text()

    page.reload()

    expect(page.get_by_test_id("order-number")).to_have_text(order_number)
