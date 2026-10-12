"""Tests for retry behaviour in APIClient.

Uses `responses` to simulate transient failures, then verify that
the retry logic automatically recovers.
"""

import contextlib

import responses

from src.api_client import BASE_URL, APIClient

# ---------------------------------------------------------------------------
# Successful retry: transient 5xx then success
# ---------------------------------------------------------------------------


@responses.activate
def test_get_retries_on_503_then_succeeds() -> None:
    """Server returns 503 twice, then 200 — client should recover."""
    # Two failures, then success
    responses.get(f"{BASE_URL}/posts/1", status=503)
    responses.get(f"{BASE_URL}/posts/1", status=503)
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Recovered", "body": "x", "userId": 1},
        status=200,
    )

    client = APIClient(max_retries=3)
    try:
        post = client.get("/posts/1")
        assert post["title"] == "Recovered"
        # Should have made 3 attempts total
        assert len(responses.calls) == 3
    finally:
        client.close()


@responses.activate
def test_get_retries_on_500_then_succeeds() -> None:
    responses.get(f"{BASE_URL}/posts/1", status=500)
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "OK", "body": "x", "userId": 1},
        status=200,
    )

    client = APIClient(max_retries=3)
    try:
        post = client.get("/posts/1")
        assert post["title"] == "OK"
        assert len(responses.calls) == 2
    finally:
        client.close()


# ---------------------------------------------------------------------------
# No retry on 4xx (client error)
# ---------------------------------------------------------------------------


@responses.activate
def test_get_does_not_retry_on_404() -> None:
    """404 means the resource doesn't exist — retrying is pointless."""
    responses.get(f"{BASE_URL}/posts/9999", status=404)

    client = APIClient(max_retries=3)
    try:
        with contextlib.suppress(Exception):
            client.get("/posts/9999")
        # Only ONE attempt — no retry
        assert len(responses.calls) == 1
    finally:
        client.close()


# ---------------------------------------------------------------------------
# Exhausted retries: gives up after max_retries
# ---------------------------------------------------------------------------


@responses.activate
def test_get_gives_up_after_max_retries() -> None:
    """If all attempts fail, the client should raise an error."""
    for _ in range(5):
        responses.get(f"{BASE_URL}/posts/1", status=503)

    client = APIClient(max_retries=2)
    try:
        with contextlib.suppress(Exception):
            client.get("/posts/1")

        # max_retries=2 → 1 initial + 2 retries = 3 attempts
        assert len(responses.calls) == 3
    finally:
        client.close()
