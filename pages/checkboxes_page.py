"""Checkboxes page object for /checkboxes."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    """Page object for /checkboxes (two checkboxes)."""

    path = "/checkboxes"

    CHECKBOXES = "input[type=checkbox]"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # --- actions --------------------------------------------------------

    def check(self, index: int) -> "CheckboxesPage":
        """Ensure the checkbox at `index` is checked."""
        box = self.page.locator(self.CHECKBOXES).nth(index)
        if not box.is_checked():
            box.check()
        return self

    def uncheck(self, index: int) -> "CheckboxesPage":
        """Ensure the checkbox at `index` is unchecked."""
        box = self.page.locator(self.CHECKBOXES).nth(index)
        if box.is_checked():
            box.uncheck()
        return self

    def toggle(self, index: int) -> "CheckboxesPage":
        """Flip the checkbox at `index`."""
        self.page.locator(self.CHECKBOXES).nth(index).click()
        return self

    # --- assertion helpers ---------------------------------------------

    def expect_checked(self, index: int) -> None:
        expect(self.page.locator(self.CHECKBOXES).nth(index)).to_be_checked()

    def expect_unchecked(self, index: int) -> None:
        expect(self.page.locator(self.CHECKBOXES).nth(index)).not_to_be_checked()
