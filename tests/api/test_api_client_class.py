"""Tests for the session-based APIClient, using pytest fixtures."""

import responses

from src.api_client import BASE_URL, APIClient

# ---------------------------------------------------------------------------
# Basic GET via fixture
# ---------------------------------------------------------------------------


@responses.activate
def test_api_get_post(api: APIClient) -> None:
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Hello", "body": "World", "userId": 1},
        status=200,
    )
    post = api.get("/posts/1")
    assert post["id"] == 1
    assert post["title"] == "Hello"


@responses.activate
def test_api_get_multiple_posts(api: APIClient) -> None:
    """Multiple GETs on the same session — connection reuse."""
    for i in [1, 2, 3]:
        responses.get(
            f"{BASE_URL}/posts/{i}",
            json={"id": i, "title": f"Post {i}", "body": "x", "userId": 1},
            status=200,
        )

    for i in [1, 2, 3]:
        assert api.get(f"/posts/{i}")["id"] == i

    assert len(responses.calls) == 3


# ---------------------------------------------------------------------------
# Bearer token fixture
# ---------------------------------------------------------------------------


@responses.activate
def test_authed_api_sends_token(authed_api: APIClient) -> None:
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Secure", "body": "x", "userId": 1},
        status=200,
    )

    authed_api.get("/posts/1")

    sent = responses.calls[0].request
    assert sent.headers["Authorization"] == "Bearer test-token-123"


# ---------------------------------------------------------------------------
# POST via session
# ---------------------------------------------------------------------------


@responses.activate
def test_api_post(api: APIClient) -> None:
    responses.post(
        f"{BASE_URL}/posts",
        json={"id": 101, "title": "New", "body": "Body", "userId": 1},
        status=201,
    )

    result = api.post("/posts", {"title": "New", "body": "Body", "userId": 1})
    assert result["id"] == 101
    assert result["title"] == "New"
