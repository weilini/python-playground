"""API tests using pytest parametrize.

Parametrize lets one test function run with many inputs — cleaner than
copy-pasting near-identical tests.
"""

import pytest
import responses

from src.api_client import (
    BASE_URL,
    create_post,
    get_post,
    get_post_status,
)

# ---------------------------------------------------------------------------
# Parametrized: get_post by ID
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("post_id", [1, 2, 5, 10, 100])
@responses.activate
def test_get_post_returns_correct_id(post_id: int) -> None:
    """One test — runs once per ID."""
    responses.get(
        f"{BASE_URL}/posts/{post_id}",
        json={"id": post_id, "title": f"Post {post_id}", "body": "x", "userId": 1},
        status=200,
    )

    post = get_post(post_id)
    assert post["id"] == post_id
    assert post["title"] == f"Post {post_id}"


# ---------------------------------------------------------------------------
# Parametrized: status codes
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "status_code",
    [200, 201, 204, 400, 401, 403, 404, 500, 503],
)
@responses.activate
def test_get_post_status_returns_server_code(status_code: int) -> None:
    """get_post_status() should return whatever the server sends."""
    responses.get(f"{BASE_URL}/posts/1", status=status_code)
    assert get_post_status(1) == status_code


# ---------------------------------------------------------------------------
# Parametrized: create_post payload combinations
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("title", "body", "user_id"),
    [
        ("Short", "Body", 1),
        ("A much longer title with spaces", "Longer body content", 2),
        ("Title with special chars: !@#$", "Body with ünïcödé", 3),
        ("", "", 1),
    ],
)
@responses.activate
def test_create_post_accepts_various_payloads(
    title: str, body: str, user_id: int
) -> None:
    responses.post(
        f"{BASE_URL}/posts",
        json={"id": 101, "title": title, "body": body, "userId": user_id},
        status=201,
    )

    post = create_post(title, body, user_id)

    assert post["title"] == title
    assert post["body"] == body
    assert post["userId"] == user_id

    # Also verify what was actually sent
    sent = responses.calls[0].request
    assert sent.method == "POST"
