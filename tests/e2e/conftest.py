"""pytest fixtures for Playwright e2e tests.

Fixtures here are automatically available to any test file inside
tests/e2e/ (and subfolders), without needing an import.
"""

import pytest
from playwright.sync_api import Page

from pages import CheckboxesPage, DropdownPage, LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Return a LoginPage already navigated to /login."""
    return LoginPage(page).open()


@pytest.fixture
def checkboxes_page(page: Page) -> CheckboxesPage:
    """Return a CheckboxesPage already navigated to /checkboxes."""
    return CheckboxesPage(page).open()


@pytest.fixture
def dropdown_page(page: Page) -> DropdownPage:
    """Return a DropdownPage already navigated to /dropdown."""
    return DropdownPage(page).open()
