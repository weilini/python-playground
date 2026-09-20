"""Tests demonstrating pytest mocking with unittest.mock.

Mocking replaces real dependencies with fake objects that
we control. This makes tests fast, reliable, and independent.
"""

from unittest.mock import Mock, patch

import pytest

from src.api_client import get_post, get_all_posts, create_post, get_post_status


# ============================================================
# Example 1 — Basic mock of requests.get
# ============================================================


@patch("src.api_client.requests.get")
def test_get_post_returns_expected_data(mock_get):
    """Test get_post without hitting the real API."""
    # Arrange: set up the fake response
    mock_get.return_value.json.return_value = {"id": 1, "title": "Test Post"}
    mock_get.return_value.raise_for_status.return_value = None

    # Act: call the function
    result = get_post(1)

    # Assert: verify the result
    assert result == {"id": 1, "title": "Test Post"}

    # Verify: the API was called once with the correct URL
    mock_get.assert_called_once()
    call_args = mock_get.call_args
    assert "posts/1" in call_args[0][0]


# ============================================================
# Example 2 — Mock an error response
# ============================================================


@patch("src.api_client.requests.get")
def test_get_post_handles_500_error(mock_get):
    """Test that get_post raises when the API returns an error."""
    import requests

    # Arrange: make raise_for_status raise an HTTPError
    mock_get.return_value.raise_for_status.side_effect = requests.HTTPError("500")

    # Act + Assert: expect an exception
    with pytest.raises(requests.HTTPError):
        get_post(1)


# ============================================================
# Example 3 — Mock returning a list
# ============================================================


@patch("src.api_client.requests.get")
def test_get_all_posts_returns_list(mock_get):
    """Test get_all_posts with a mocked response."""
    # Arrange: mock 3 posts instead of 100
    mock_get.return_value.json.return_value = [
        {"id": 1, "title": "Post 1"},
        {"id": 2, "title": "Post 2"},
        {"id": 3, "title": "Post 3"},
    ]
    mock_get.return_value.raise_for_status.return_value = None

    # Act
    result = get_all_posts()

    # Assert
    assert len(result) == 3
    assert result[0]["title"] == "Post 1"


# ============================================================
# Example 4 — Mock a POST request
# ============================================================


@patch("src.api_client.requests.post")
def test_create_post_sends_correct_payload(mock_post):
    """Test that create_post sends the correct data."""
    # Arrange
    mock_post.return_value.json.return_value = {"id": 101, "title": "New Post"}
    mock_post.return_value.raise_for_status.return_value = None

    # Act
    result = create_post("New Post", "Body text", 1)

    # Assert
    assert result["id"] == 101

    # Verify: check what was sent to requests.post
    mock_post.assert_called_once()
    call_kwargs = mock_post.call_args.kwargs
    assert call_kwargs["json"]["title"] == "New Post"
    assert call_kwargs["json"]["body"] == "Body text"
    assert call_kwargs["json"]["userId"] == 1


# ============================================================
# Example 5 — Test status code without real request
# ============================================================


@patch("src.api_client.requests.get")
def test_get_post_status_404(mock_get):
    """Test that get_post_status returns 404 for invalid ID."""
    # Arrange: mock a 404 response
    mock_get.return_value.status_code = 404

    # Act
    status = get_post_status(9999)

    # Assert
    assert status == 404


# ============================================================
# Example 6 — Mocking multiple calls
# ============================================================


@patch("src.api_client.requests.get")
def test_multiple_calls_different_responses(mock_get):
    """Test that different calls can return different responses."""
    # Arrange: first call returns 200, second returns 404
    mock_get.side_effect = [
        Mock(json=lambda: {"id": 1}, status_code=200, raise_for_status=lambda: None),
        Mock(json=lambda: {}, status_code=404, raise_for_status=lambda: None),
    ]

    # Act
    first = get_post_status(1)
    second = get_post_status(9999)

    # Assert
    assert first == 200
    assert second == 404
    assert mock_get.call_count == 2


# ============================================================
# Example 7 — Mock a date/time
# ============================================================


@patch("src.api_client.requests.get")
def test_mock_example_for_future_use(mock_get):
    """Placeholder to show how mocking extends beyond APIs.

    In the future, you can mock datetime, random, file systems, etc.
    """
    # This test always passes — it's just a pattern
    assert True


# ============================================================
# Example 8 — Mock with patch.object
# ============================================================


def test_patch_object_example():
    """Show patch.object for patching methods on objects."""
    fake_client = Mock()
    fake_client.get.return_value = {"status": "ok"}

    result = fake_client.get("/health")

    assert result["status"] == "ok"
    fake_client.get.assert_called_once_with("/health")
