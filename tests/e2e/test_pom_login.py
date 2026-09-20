"""Stage 4 Day 5 — Tests using the Page Object Model.

These tests demonstrate how page objects make tests shorter and more
readable. Compare with test_locators.py and test_assertions.py: same
functionality, but page details live in pages/, not in the tests.
"""

from playwright.sync_api import Page

from pages import CheckboxesPage, DropdownPage, LoginPage

# ---------------------------------------------------------------------------
# LoginPage
# ---------------------------------------------------------------------------


class TestLoginPage:
    def test_successful_login(self, page: Page) -> None:
        login = LoginPage(page).open()
        login.login("tomsmith", "SuperSecretPassword!")
        login.expect_success_message()
        login.expect_url_contains("/secure")

    def test_failed_login_shows_error(self, page: Page) -> None:
        login = LoginPage(page).open()
        login.login("wronguser", "wrongpass")
        login.expect_error_message()

    def test_login_heading(self, page: Page) -> None:
        login = LoginPage(page).open()
        login.expect_heading("Login Page")

    def test_logout_returns_to_login(self, page: Page) -> None:
        login = LoginPage(page).open()
        login.login("tomsmith", "SuperSecretPassword!")
        page.click("a[href='/logout']")
        login.expect_url_contains("/login")


# ---------------------------------------------------------------------------
# CheckboxesPage
# ---------------------------------------------------------------------------


class TestCheckboxesPage:
    def test_initial_state(self, page: Page) -> None:
        boxes = CheckboxesPage(page).open()
        boxes.expect_unchecked(0)
        boxes.expect_checked(1)

    def test_check_first_checkbox(self, page: Page) -> None:
        boxes = CheckboxesPage(page).open()
        boxes.check(0)
        boxes.expect_checked(0)

    def test_uncheck_second_checkbox(self, page: Page) -> None:
        boxes = CheckboxesPage(page).open()
        boxes.uncheck(1)
        boxes.expect_unchecked(1)

    def test_toggle_both(self, page: Page) -> None:
        boxes = CheckboxesPage(page).open()
        boxes.toggle(0).toggle(1)
        boxes.expect_checked(0)
        boxes.expect_unchecked(1)


# ---------------------------------------------------------------------------
# DropdownPage
# ---------------------------------------------------------------------------


class TestDropdownPage:
    def test_select_by_label(self, page: Page) -> None:
        dd = DropdownPage(page).open()
        dd.select_by_label("Option 1")
        dd.expect_selected_label("Option 1")

    def test_select_by_value(self, page: Page) -> None:
        dd = DropdownPage(page).open()
        dd.select_by_value("2")
        dd.expect_selected_label("Option 2")
