"""Login page object for the-internet.herokuapp.com/login.

Encapsulates all locators and actions for the login page so tests
can read like English and stay resilient to page changes.
"""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for /login."""

    path = "/login"

    # --- locators (defined once, reused everywhere) ---------------------

    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "button[type=submit]"
    FLASH_MESSAGE = "#flash"
    HEADING = "h2"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # --- actions --------------------------------------------------------

    def fill_username(self, username: str) -> "LoginPage":
        self.page.fill(self.USERNAME_INPUT, username)
        return self

    def fill_password(self, password: str) -> "LoginPage":
        self.page.fill(self.PASSWORD_INPUT, password)
        return self

    def submit(self) -> "LoginPage":
        self.page.click(self.SUBMIT_BUTTON)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """Full login flow in one call — most tests will use this."""
        return self.fill_username(username).fill_password(password).submit()

    # --- assertion helpers ---------------------------------------------

    def expect_heading(self, text: str) -> None:
        expect(self.page.locator(self.HEADING)).to_have_text(text)

    def expect_success_message(self) -> None:
        expect(self.page.locator(self.FLASH_MESSAGE)).to_contain_text(
            "You logged into a secure area!"
        )

    def expect_error_message(self) -> None:
        expect(self.page.locator(self.FLASH_MESSAGE)).to_contain_text(
            "Your username is invalid!"
        )
