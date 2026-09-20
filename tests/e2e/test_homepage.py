"""First Playwright tests — UI automation."""

import re

import pytest
from playwright.sync_api import Page, expect


def test_python_org_homepage_loads(page: Page) -> None:
    """Test that python.org loads and shows the title."""
    page.goto("https://www.python.org/")

    # Use a regex pattern (not a lambda)
    expect(page).to_have_title(re.compile(r"Python"))


def test_python_org_has_donate_link(page: Page) -> None:
    """Test that the Donate button exists on python.org."""
    page.goto("https://www.python.org/")

    # Use exact=True to match "Donate" but not "Donate to the PSF"
    donate_link = page.get_by_role("link", name="Donate", exact=True)
    expect(donate_link).to_be_visible()


def test_python_org_navigate_to_docs(page: Page) -> None:
    """Test navigation from homepage to docs page."""
    page.goto("https://www.python.org/")

    # Click the "Docs" link
    page.get_by_role("link", name="Docs").first.click()

    # Wait for navigation to complete
    page.wait_for_load_state("load")

    # Verify the URL contains docs.python.org
    assert "docs.python.org" in page.url


def test_python_org_has_navigation_menu(page: Page) -> None:
    """Test that the top navigation is present."""
    page.goto("https://www.python.org/")

    # Use .first to avoid strict mode violation
    downloads_link = page.get_by_role("link", name="Downloads").first
    expect(downloads_link).to_be_visible()

    docs_link = page.get_by_role("link", name="Documentation").first
    expect(docs_link).to_be_visible()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
