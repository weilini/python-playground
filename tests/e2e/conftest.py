"""pytest fixtures for Playwright e2e tests.

E2E tests are skipped by default because they depend on an external
site (the-internet.herokuapp.com) that is unreliable from CI and from
some networks.

To run e2e tests locally, set: RUN_E2E=1 pytest tests/e2e/
"""

import os

import pytest
from playwright.sync_api import Page

from pages import CheckboxesPage, DropdownPage, LoginPage

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Skip e2e tests unless RUN_E2E=1 is explicitly set
# ---------------------------------------------------------------------------

_RUN_E2E = os.getenv("RUN_E2E") == "1"


def pytest_collection_modifyitems(config: pytest.Config, items: list) -> None:
    """Skip e2e tests unless RUN_E2E=1."""
    if _RUN_E2E:
        return
    skip_marker = pytest.mark.skip(reason="e2e tests disabled (set RUN_E2E=1 to run)")
    for item in items:
        if "e2e" in str(item.fspath):
            item.add_marker(skip_marker)
