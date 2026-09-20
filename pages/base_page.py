"""Base page object — shared helpers for all page objects.

Every page object inherits from BasePage to get common behaviour:
navigation, waiting helpers, and access to the Playwright `page` object.
"""

import re
from typing import Self

from playwright.sync_api import Page, expect

BASE_URL = "https://the-internet.herokuapp.com"


class BasePage:
    """Common functionality shared by all page objects."""

    # Subclasses override this with their own path (e.g. "/login")
    path: str = "/"

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- navigation -----------------------------------------------------

    def open(self) -> Self:
        """Navigate to this page's URL and return self for chaining."""
        self.page.goto(f"{BASE_URL}{self.path}")
        return self

    def current_url(self) -> str:
        return self.page.url

    # --- generic assertions ---------------------------------------------

    def expect_url_contains(self, fragment: str) -> None:
        expect(self.page).to_have_url(re.compile(f".*{re.escape(fragment)}.*"))

    def expect_title(self, title: str) -> None:
        expect(self.page).to_have_title(title)
