"""Stage 4 Day 4 — Playwright assertion patterns.

Covers:
- Web-first (auto-retrying) assertions
- Non-retrying Python asserts
- Soft assertions
- Negative assertions
- Auto-retry behaviour demonstration
"""

import re

from playwright.sync_api import Page, expect

BASE = "https://the-internet.herokuapp.com"


# ---------------------------------------------------------------------------
# 1. Web-first assertions (auto-retry until timeout, default 5s)
# ---------------------------------------------------------------------------


class TestWebFirstAssertions:
    def test_text_assertion(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        expect(page.locator("h2")).to_have_text("Login Page")

    def test_visibility(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        expect(page.locator("#login")).to_be_visible()
        expect(page.locator("button[type=submit]")).to_be_enabled()

    def test_title_and_url(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        expect(page).to_have_title(re.compile(r"The Internet"))
        expect(page).to_have_url(f"{BASE}/login")

    def test_input_value_after_typing(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        page.fill("#username", "tomsmith")
        expect(page.locator("#username")).to_have_value("tomsmith")


# ---------------------------------------------------------------------------
# 2. Non-retrying Python assert (instant, no auto-retry)
# ---------------------------------------------------------------------------


class TestNonRetryingAssert:
    def test_python_assert_on_heading(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        heading = page.locator("h2").inner_text()
        assert heading == "Login Page"

    def test_python_assert_on_count(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        buttons = page.locator("button").count()
        assert buttons == 1


# ---------------------------------------------------------------------------
# 3. Soft assertions (collect multiple failures, don't stop at first)
# ---------------------------------------------------------------------------


class TestSoftAssertions:
    def test_checkboxes_soft(self, page: Page) -> None:
        page.goto(f"{BASE}/checkboxes")
        boxes = page.locator("input[type=checkbox]")
        expect.soft(boxes.nth(0)).not_to_be_checked()
        expect.soft(boxes.nth(1)).to_be_checked()

    def test_login_form_soft(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        expect.soft(page.locator("#username")).to_be_visible()
        expect.soft(page.locator("#password")).to_be_visible()
        expect.soft(page.locator("button[type=submit]")).to_be_enabled()


# ---------------------------------------------------------------------------
# 4. Negative assertions
# ---------------------------------------------------------------------------


class TestNegativeAssertions:
    def test_error_flash_not_visible_on_load(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        expect(page.locator(".flash.error")).not_to_be_visible()

    def test_h1_has_zero_count(self, page: Page) -> None:
        page.goto(f"{BASE}/login")
        expect(page.locator("h1")).to_have_count(0)


# ---------------------------------------------------------------------------
# 5. Auto-retry demonstration — no time.sleep() needed
# ---------------------------------------------------------------------------


class TestAutoRetry:
    def test_dynamic_element_appears(self, page: Page) -> None:
        page.goto(f"{BASE}/dynamic_loading/1")
        page.click("#start button")
        # expect() retries for up to 5s — element appears asynchronously
        expect(page.locator("#finish h4")).to_have_text("Hello World!")

    def test_custom_timeout(self, page: Page) -> None:
        page.goto(f"{BASE}/dynamic_loading/2")
        page.click("#start button")
        expect(page.locator("#finish h4")).to_have_text("Hello World!", timeout=10_000)
