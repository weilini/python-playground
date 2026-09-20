"""Stage 4 Day 5-6 — Tests using Page Object Model + pytest fixtures.

Uses fixtures from conftest.py: login_page, checkboxes_page, dropdown_page.
Each fixture returns a page object already navigated to its page, so
tests contain only behaviour — no setup boilerplate.
"""

from playwright.sync_api import Page

from pages import CheckboxesPage, DropdownPage, LoginPage

# ---------------------------------------------------------------------------
# LoginPage
# ---------------------------------------------------------------------------


class TestLoginPage:
    def test_successful_login(self, login_page: LoginPage) -> None:
        login_page.login("tomsmith", "SuperSecretPassword!")
        login_page.expect_success_message()
        login_page.expect_url_contains("/secure")

    def test_failed_login_shows_error(self, login_page: LoginPage) -> None:
        login_page.login("wronguser", "wrongpass")
        login_page.expect_error_message()

    def test_login_heading(self, login_page: LoginPage) -> None:
        login_page.expect_heading("Login Page")

    def test_logout_returns_to_login(self, page: Page, login_page: LoginPage) -> None:
        login_page.login("tomsmith", "SuperSecretPassword!")
        page.click("a[href='/logout']")
        login_page.expect_url_contains("/login")


# ---------------------------------------------------------------------------
# CheckboxesPage
# ---------------------------------------------------------------------------


class TestCheckboxesPage:
    def test_initial_state(self, checkboxes_page: CheckboxesPage) -> None:
        checkboxes_page.expect_unchecked(0)
        checkboxes_page.expect_checked(1)

    def test_check_first_checkbox(self, checkboxes_page: CheckboxesPage) -> None:
        checkboxes_page.check(0)
        checkboxes_page.expect_checked(0)

    def test_uncheck_second_checkbox(self, checkboxes_page: CheckboxesPage) -> None:
        checkboxes_page.uncheck(1)
        checkboxes_page.expect_unchecked(1)

    def test_toggle_both(self, checkboxes_page: CheckboxesPage) -> None:
        checkboxes_page.toggle(0).toggle(1)
        checkboxes_page.expect_checked(0)
        checkboxes_page.expect_unchecked(1)


# ---------------------------------------------------------------------------
# DropdownPage
# ---------------------------------------------------------------------------


class TestDropdownPage:
    def test_select_by_label(self, dropdown_page: DropdownPage) -> None:
        dropdown_page.select_by_label("Option 1")
        dropdown_page.expect_selected_label("Option 1")

    def test_select_by_value(self, dropdown_page: DropdownPage) -> None:
        dropdown_page.select_by_value("2")
        dropdown_page.expect_selected_label("Option 2")
