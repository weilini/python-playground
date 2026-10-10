"""API tests for authentication and custom headers.

Uses `responses` to mock HTTP calls — no real network requests.
"""

import base64

import responses
from requests.exceptions import HTTPError

from src.api_client import (
    BASE_URL,
    get_protected_resource,
    get_with_basic_auth,
    get_with_custom_headers,
)

# ---------------------------------------------------------------------------
# Bearer token auth
# ---------------------------------------------------------------------------


@responses.activate
def test_bearer_token_is_sent_in_header() -> None:
    """The Authorization header must contain the exact Bearer token."""
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Protected", "body": "Secret", "userId": 1},
        status=200,
    )

    get_protected_resource("my-secret-token")

    assert len(responses.calls) == 1
    sent = responses.calls[0].request
    assert sent.headers["Authorization"] == "Bearer my-secret-token"


@responses.activate
def test_bearer_token_401_raises() -> None:
    """An invalid/expired token returns 401 — raise HTTPError."""
    responses.get(f"{BASE_URL}/posts/1", status=401)

    try:
        get_protected_resource("expired-token")
    except HTTPError:
        pass
    else:
        raise AssertionError("Expected HTTPError for 401 response")


@responses.activate
def test_bearer_token_403_raises() -> None:
    """A valid token with wrong scope returns 403."""
    responses.get(f"{BASE_URL}/posts/1", status=403)

    try:
        get_protected_resource("valid-but-forbidden-token")
    except HTTPError:
        pass
    else:
        raise AssertionError("Expected HTTPError for 403 response")


# ---------------------------------------------------------------------------
# Basic auth
# ---------------------------------------------------------------------------


@responses.activate
def test_basic_auth_header_is_base64_encoded() -> None:
    """`requests` must encode user:pass as base64 in the Authorization header."""
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Basic", "body": "Auth", "userId": 1},
        status=200,
    )

    get_with_basic_auth("alice", "s3cret")

    sent = responses.calls[0].request
    expected = base64.b64encode(b"alice:s3cret").decode()
    assert sent.headers["Authorization"] == f"Basic {expected}"


@responses.activate
def test_basic_auth_wrong_credentials_401() -> None:
    responses.get(f"{BASE_URL}/posts/1", status=401)

    try:
        get_with_basic_auth("alice", "wrong")
    except HTTPError:
        pass
    else:
        raise AssertionError("Expected HTTPError for 401 response")


# ---------------------------------------------------------------------------
# Custom headers
# ---------------------------------------------------------------------------


@responses.activate
def test_custom_api_key_header_is_sent() -> None:
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Key", "body": "Value", "userId": 1},
        status=200,
    )

    get_with_custom_headers({"X-API-Key": "abc-123", "Accept": "application/json"})

    sent = responses.calls[0].request
    assert sent.headers["X-API-Key"] == "abc-123"
    assert sent.headers["Accept"] == "application/json"


@responses.activate
def test_multiple_custom_headers() -> None:
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Multi", "body": "Headers", "userId": 1},
        status=200,
    )

    headers = {
        "X-API-Key": "key-xyz",
        "X-Request-ID": "req-001",
        "User-Agent": "my-test-client/1.0",
    }
    get_with_custom_headers(headers)

    sent = responses.calls[0].request
    assert sent.headers["X-API-Key"] == "key-xyz"
    assert sent.headers["X-Request-ID"] == "req-001"
    assert sent.headers["User-Agent"] == "my-test-client/1.0"
