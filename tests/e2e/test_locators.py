"""Playwright locator tests — demonstrating the 6 locator types.

These tests use the-internet.herokuapp.com — a public site
designed for automation practice.
"""

import re

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://the-internet.herokuapp.com"


class TestLocatorTypes:
    """Demonstrate each locator type on a real site."""

    def test_get_by_role_link(self, page: Page) -> None:
        """Find a link by its role and name."""
        page.goto(BASE_URL)

        # Find the "Form Authentication" link on the homepage
        link = page.get_by_role("link", name="Form Authentication")
        expect(link).to_be_visible()

    def test_get_by_role_heading(self, page: Page) -> None:
        """Find a heading by role."""
        page.goto(f"{BASE_URL}/login")

        # The page has an <h2> with text "Login Page"
        heading = page.get_by_role("heading", name="Login Page")
        expect(heading).to_be_visible()

    def test_get_by_label_for_username(self, page: Page) -> None:
        """Find an input field by its label."""
        page.goto(f"{BASE_URL}/login")

        # The username input has a <label>Username</label>
        username_input = page.get_by_label("Username")
        expect(username_input).to_be_visible()

    def test_get_by_label_for_password(self, page: Page) -> None:
        """Find password input by its label."""
        page.goto(f"{BASE_URL}/login")

        password_input = page.get_by_label("Password")
        expect(password_input).to_be_visible()

    def test_get_by_text_for_flash_message(self, page: Page) -> None:
        """Find text content."""
        page.goto(f"{BASE_URL}/login")

        # The page has a heading "Login Page" (text)
        expect(page.get_by_text("Login Page", exact=True)).to_be_visible()

    def test_get_by_role_button(self, page: Page) -> None:
        """Find a button by role."""
        page.goto(f"{BASE_URL}/login")

        # The submit button has <button type="submit">Login</button>
        submit_button = page.get_by_role("button", name="Login")
        expect(submit_button).to_be_visible()


class TestLocatorModifiers:
    """Demonstrate locator modifiers."""

    def test_first_selector(self, page: Page) -> None:
        """Use .first to get the first matching element."""
        page.goto(BASE_URL)

        # The homepage has multiple links to the same pages
        # .first picks the first one
        first_link = page.get_by_role("link", name="Form Authentication").first
        expect(first_link).to_be_visible()

    def test_nth_selector(self, page: Page) -> None:
        """Use .nth to get the nth matching element."""
        page.goto(BASE_URL)

        # Get all the list item links and pick the 2nd (index 1)
        all_links = page.locator("ul li a")
        # We just check that the 2nd one is visible
        expect(all_links.nth(1)).to_be_visible()

    def test_filter_has_text(self, page: Page) -> None:
        """Filter locators by text content."""
        page.goto(BASE_URL)

        # Find all h2 headings that contain "Available Examples"
        heading = page.locator("h2").filter(has_text="Available Examples")
        expect(heading).to_be_visible()


class TestLoginFlow:
    """Test a complete login workflow using locators."""

    def test_successful_login(self, page: Page) -> None:
        """Test the full login flow with valid credentials."""
        page.goto(f"{BASE_URL}/login")

        # Fill username
        page.get_by_label("Username").fill("tomsmith")

        # Fill password
        page.get_by_label("Password").fill("SuperSecretPassword!")

        # Click the Login button
        page.get_by_role("button", name="Login").click()

        # Verify we landed on the secure area
        expect(page).to_have_url(re.compile(r"/secure"))
        expect(page.get_by_text("You logged into a secure area!")).to_be_visible()

    def test_failed_login_shows_error(self, page: Page) -> None:
        """Test that wrong credentials show an error message."""
        page.goto(f"{BASE_URL}/login")

        page.get_by_label("Username").fill("wronguser")
        page.get_by_label("Password").fill("wrongpass")
        page.get_by_role("button", name="Login").click()

        # Error flash message
        expect(page.get_by_text("Your username is invalid!")).to_be_visible()

    def test_logout(self, page: Page) -> None:
        """Test logging out after successful login."""
        page.goto(f"{BASE_URL}/login")

        # Login
        page.get_by_label("Username").fill("tomsmith")
        page.get_by_label("Password").fill("SuperSecretPassword!")
        page.get_by_role("button", name="Login").click()

        # Wait for secure area
        page.wait_for_url(re.compile(r"/secure"))

        # Click logout
        page.get_by_role("link", name="Logout").click()

        # Verify back on login page
        expect(page.get_by_text("You logged out of the secure area!")).to_be_visible()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
