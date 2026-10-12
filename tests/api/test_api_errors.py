"""API tests for error handling.

Tests how the API client behaves when things go wrong:
- HTTP errors (4xx, 5xx)
- Timeouts
- Connection failures
- Invalid JSON responses
"""

import pytest
import responses
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import HTTPError, JSONDecodeError, Timeout

from src.api_client import BASE_URL, get_post, get_post_status

# ---------------------------------------------------------------------------
# HTTP errors (4xx / 5xx) — should raise HTTPError via raise_for_status()
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("status_code", [400, 401, 403, 404, 500, 502, 503])
@responses.activate
def test_get_post_raises_http_error_on_4xx_5xx(status_code: int) -> None:
    responses.get(f"{BASE_URL}/posts/1", status=status_code)

    with pytest.raises(HTTPError):
        get_post(1)


@responses.activate
def test_get_post_status_does_not_raise_on_500() -> None:
    """get_post_status() doesn't call raise_for_status — should return 500."""
    responses.get(f"{BASE_URL}/posts/1", status=500)
    assert get_post_status(1) == 500


# ---------------------------------------------------------------------------
# Timeouts
# ---------------------------------------------------------------------------


@responses.activate
def test_get_post_raises_timeout_when_server_slow() -> None:
    responses.get(f"{BASE_URL}/posts/1", body=Timeout("Connection timed out"))

    with pytest.raises(Timeout):
        get_post(1)


# ---------------------------------------------------------------------------
# Connection failures (server unreachable)
# ---------------------------------------------------------------------------


@responses.activate
def test_get_post_raises_connection_error_when_server_down() -> None:
    responses.get(
        f"{BASE_URL}/posts/1",
        body=RequestsConnectionError("Connection refused"),
    )

    with pytest.raises(RequestsConnectionError):
        get_post(1)


# ---------------------------------------------------------------------------
# Invalid JSON responses
# ---------------------------------------------------------------------------


@responses.activate
def test_get_post_raises_json_decode_error_on_invalid_body() -> None:
    """Server returns 200 but body isn't valid JSON."""
    responses.get(
        f"{BASE_URL}/posts/1",
        body="this is not json {{{",
        status=200,
        content_type="application/json",
    )

    with pytest.raises(JSONDecodeError):
        get_post(1)


# ---------------------------------------------------------------------------
# Empty body
# ---------------------------------------------------------------------------


@responses.activate
def test_get_post_raises_json_decode_error_on_empty_body() -> None:
    responses.get(f"{BASE_URL}/posts/1", body="", status=200)
    with pytest.raises(JSONDecodeError):
        get_post(1)
