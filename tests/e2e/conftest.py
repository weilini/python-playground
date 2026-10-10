"""pytest fixtures for Playwright e2e tests.

Fixtures here are automatically available to any test file inside
tests/e2e/ (and subfolders), without needing an import.

Also skips all e2e tests if the target site is unreachable (e.g. in CI).
"""

import pytest
import requests
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
# Skip all e2e tests if the test site is unreachable (e.g. in CI)
# ---------------------------------------------------------------------------

_TARGET_URL = "https://the-internet.herokuapp.com/"


def _site_is_reachable(url: str, timeout: float = 5.0) -> bool:
    """Return True if we get any non-5xx HTTP response from the URL."""
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code < 500
    except Exception:
        return False


_SITE_UP = _site_is_reachable(_TARGET_URL)


def pytest_collection_modifyitems(config: pytest.Config, items: list) -> None:
    """If the e2e test site is unreachable, skip all e2e tests."""
    if _SITE_UP:
        return
    skip_marker = pytest.mark.skip(
        reason=f"{_TARGET_URL} unreachable - skipping e2e tests"
    )
    for item in items:
        if "e2e" in str(item.fspath):
            item.add_marker(skip_marker)
