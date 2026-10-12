"""pytest fixtures for API tests."""

from collections.abc import Generator

import pytest

from src.api_client import APIClient


@pytest.fixture
def api() -> Generator[APIClient, None, None]:
    """Return a fresh APIClient for each test."""
    client = APIClient()
    yield client
    client.close()


@pytest.fixture
def authed_api() -> Generator[APIClient, None, None]:
    """Return an APIClient with a Bearer token pre-configured."""
    client = APIClient(token="test-token-123")
    yield client
    client.close()
