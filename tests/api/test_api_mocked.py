"""API tests using `responses` to mock HTTP calls.

These tests do NOT hit the real JSONPlaceholder API. `responses`
intercepts requests and returns pre-defined data — fast and reliable.
"""

import responses
from requests.exceptions import HTTPError

from src.api_client import (
    BASE_URL,
    create_post,
    delete_post,
    get_post,
    get_post_status,
)

# ---------------------------------------------------------------------------
# GET /posts/{id}
# ---------------------------------------------------------------------------


@responses.activate
def test_get_post_returns_mocked_data() -> None:
    """get_post() returns the JSON the server sends — no real network."""
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Mocked Title", "body": "Mocked Body", "userId": 7},
        status=200,
    )

    post = get_post(1)

    assert post["id"] == 1
    assert post["title"] == "Mocked Title"
    assert post["body"] == "Mocked Body"
    assert post["userId"] == 7


@responses.activate
def test_get_post_404_raises_http_error() -> None:
    """A 404 from the server should raise HTTPError (via raise_for_status)."""
    responses.get(f"{BASE_URL}/posts/9999", status=404)

    try:
        get_post(9999)
    except HTTPError:
        pass
    else:
        raise AssertionError("Expected HTTPError for 404 response")


@responses.activate
def test_get_post_status_returns_500() -> None:
    """get_post_status() should return whatever status the server sends."""
    responses.get(f"{BASE_URL}/posts/1", status=500)
    assert get_post_status(1) == 500


# ---------------------------------------------------------------------------
# POST /posts
# ---------------------------------------------------------------------------


@responses.activate
def test_create_post_sends_correct_payload() -> None:
    """create_post() should POST the correct JSON payload."""
    responses.post(
        f"{BASE_URL}/posts",
        json={"id": 101, "title": "My Post", "body": "Body", "userId": 1},
        status=201,
    )

    post = create_post("My Post", "Body", 1)

    # Verify the request that was sent
    assert len(responses.calls) == 1
    sent = responses.calls[0].request
    assert sent.method == "POST"
    assert "application/json" in sent.headers.get("Content-Type", "")

    # Verify the response was parsed correctly
    assert post["id"] == 101
    assert post["title"] == "My Post"


# ---------------------------------------------------------------------------
# DELETE /posts/{id}
# ---------------------------------------------------------------------------


@responses.activate
def test_delete_post_returns_200() -> None:
    responses.delete(f"{BASE_URL}/posts/1", status=200)
    assert delete_post(1) == 200
