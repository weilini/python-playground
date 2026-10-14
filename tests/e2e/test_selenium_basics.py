"""Selenium basics — comparison with Playwright.

Demonstrates core Selenium API. Selenium is older and more verbose
than Playwright, but widely used in enterprise environments.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    """Create a headless Chrome driver for testing."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/usr/bin/chromedriver")
    d = webdriver.Chrome(options=options, service=service)
    yield d
    d.quit()


def test_selenium_opens_page(driver):
    """Open a page and check title."""
    driver.get("https://example.com")
    assert "Example Domain" in driver.title


def test_selenium_finds_element_by_tag(driver):
    """Find the title tag with explicit wait."""
    driver.get("https://example.com")
    title = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "title"))
    )
    assert "Example Domain" in title.get_attribute("textContent")


def test_selenium_finds_element_by_xpath(driver):
    """Find by XPath with explicit wait."""
    driver.get("https://example.com")
    title = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//title"))
    )
    assert "Example Domain" in title.get_attribute("textContent")


def test_selenium_check_url(driver):
    """Check the current URL."""
    driver.get("https://example.com")
    assert driver.current_url == "https://example.com/"


def test_selenium_get_page_source(driver):
    """Get raw page source — useful for debugging."""
    driver.get("https://example.com")
    source = driver.page_source
    assert "Example Domain" in source
