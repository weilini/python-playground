"""Dropdown page object for /dropdown."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DropdownPage(BasePage):
    """Page object for /dropdown (single-select)."""

    path = "/dropdown"

    SELECT = "#dropdown"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # --- actions --------------------------------------------------------

    def select_by_label(self, label: str) -> "DropdownPage":
        self.page.select_option(self.SELECT, label=label)
        return self

    def select_by_value(self, value: str) -> "DropdownPage":
        self.page.select_option(self.SELECT, value=value)
        return self

    # --- assertion helpers ---------------------------------------------

    def expect_selected_label(self, label: str) -> None:
        expect(self.page.locator(f"{self.SELECT} option:checked")).to_have_text(label)
