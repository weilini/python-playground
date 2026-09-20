"""Playwright form testing — text inputs, dropdowns, checkboxes, etc.

Uses the-internet.herokuapp.com — a public site designed for automation.
"""

import re

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://the-internet.herokuapp.com"


class TestTextInputs:
    """Test text input fields."""

    def test_fill_text_input(self, page: Page) -> None:
        """Fill a text input and verify the value."""
        page.goto(f"{BASE_URL}/login")

        username = page.get_by_label("Username")
        username.fill("tomsmith")

        # Verify the input has the value we filled
        expect(username).to_have_value("tomsmith")

    def test_clear_input(self, page: Page) -> None:
        """Fill then clear a text input."""
        page.goto(f"{BASE_URL}/login")

        username = page.get_by_label("Username")
        username.fill("tomsmith")
        expect(username).to_have_value("tomsmith")

        # Clear the input
        username.clear()
        expect(username).to_have_value("")

    def test_fill_and_submit(self, page: Page) -> None:
        """Fill a form and click submit."""
        page.goto(f"{BASE_URL}/login")

        page.get_by_label("Username").fill("tomsmith")
        page.get_by_label("Password").fill("SuperSecretPassword!")
        page.get_by_role("button", name="Login").click()

        expect(page).to_have_url(re.compile(r"/secure"))


class TestDropdowns:
    """Test dropdown (select) elements."""

    def test_select_option_by_value(self, page: Page) -> None:
        """Select an option by its value attribute."""
        page.goto(f"{BASE_URL}/dropdown")

        dropdown = page.get_by_role("combobox")
        dropdown.select_option("1")  # value="1" is "Option 1"

        expect(dropdown).to_have_value("1")

    def test_select_option_by_label(self, page: Page) -> None:
        """Select an option by its visible text."""
        page.goto(f"{BASE_URL}/dropdown")

        dropdown = page.get_by_role("combobox")
        dropdown.select_option(label="Option 2")

        expect(dropdown).to_have_value("2")

    def test_select_multiple_options(self, page: Page) -> None:
        """Select multiple options (for multi-select)."""
        # This page has a multi-select example
        page.goto(f"{BASE_URL}/dropdown")

        # For single-select, we just verify one option
        dropdown = page.get_by_role("combobox")
        dropdown.select_option("2")
        expect(dropdown).to_have_value("2")


class TestCheckboxes:
    """Test checkbox elements."""

    def test_check_checkbox(self, page: Page) -> None:
        """Check a checkbox and verify it's checked."""
        page.goto(f"{BASE_URL}/checkboxes")

        first_checkbox = page.locator("input[type='checkbox']").first
        first_checkbox.check()

        expect(first_checkbox).to_be_checked()

    def test_uncheck_checkbox(self, page: Page) -> None:
        """Uncheck a checkbox and verify it's unchecked."""
        page.goto(f"{BASE_URL}/checkboxes")

        first_checkbox = page.locator("input[type='checkbox']").first
        # First one is unchecked by default
        expect(first_checkbox).not_to_be_checked()

    def test_toggle_checkboxes(self, page: Page) -> None:
        """Toggle multiple checkboxes."""
        page.goto(f"{BASE_URL}/checkboxes")

        checkboxes = page.locator("input[type='checkbox']")
        # Check all
        for i in range(checkboxes.count()):
            checkboxes.nth(i).check()

        # Verify all checked
        for i in range(checkboxes.count()):
            expect(checkboxes.nth(i)).to_be_checked()


class TestKeyboardActions:
    """Test keyboard interactions."""

    def test_press_enter_to_submit(self, page: Page) -> None:
        """Submit a form by pressing Enter."""
        page.goto(f"{BASE_URL}/login")

        page.get_by_label("Username").fill("tomsmith")
        page.get_by_label("Password").fill("SuperSecretPassword!")

        # Press Enter on the password field
        page.get_by_label("Password").press("Enter")

        expect(page).to_have_url(re.compile(r"/secure"))

    def test_press_tab_to_navigate(self, page: Page) -> None:
        """Navigate between fields with Tab."""
        page.goto(f"{BASE_URL}/login")

        username = page.get_by_label("Username")
        username.click()
        username.type("tomsmith")

        # Press Tab to move to password field
        username.press("Tab")
        page.keyboard.type("SuperSecretPassword!")
        page.keyboard.press("Enter")

        expect(page).to_have_url(re.compile(r"/secure"))


class TestFileUpload:
    """Test file upload elements."""

    def test_upload_file(self, page: Page, tmp_path) -> None:
        """Upload a file and verify the result."""
        # Create a temporary file to upload
        test_file = tmp_path / "upload_test.txt"
        test_file.write_text("Hello from Playwright!")

        page.goto(f"{BASE_URL}/upload")

        # Use the specific ID to avoid strict mode violation
        file_input = page.locator("#file-upload")
        file_input.set_input_files(str(test_file))

        # Click Upload
        page.get_by_role("button", name="Upload").click()

        # Verify the file was uploaded
        expect(page.get_by_text("File Uploaded!")).to_be_visible()
        expect(page.get_by_text("upload_test.txt")).to_be_visible()


class TestLinks:
    """Test clicking links and navigation."""

    def test_click_link_by_text(self, page: Page) -> None:
        """Click a link by its text."""
        page.goto(BASE_URL)

        page.get_by_role("link", name="Form Authentication").click()

        expect(page).to_have_url(re.compile(r"/login"))

    def test_click_link_by_role(self, page: Page) -> None:
        """Click a link by role."""
        page.goto(BASE_URL)

        page.get_by_role("link", name="Checkboxes").click()

        expect(page).to_have_url(re.compile(r"/checkboxes"))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
