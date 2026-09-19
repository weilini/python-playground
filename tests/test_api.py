"""Tests for src/api_client.py — JSONPlaceholder API tests."""

import pytest

from src.api_client import (
    create_post,
    get_all_posts,
    get_post,
    get_post_status,
)


class TestGetPost:
    """Tests for fetching a single post."""

    def test_get_valid_post_returns_data(self):
        post = get_post(1)
        assert post["id"] == 1
        assert "title" in post
        assert "body" in post
        assert "userId" in post

    def test_get_valid_post_returns_200(self):
        assert get_post_status(1) == 200

    def test_get_invalid_post_returns_404(self):
        assert get_post_status(9999) == 404


class TestGetAllPosts:
    """Tests for fetching all posts."""

    def test_get_all_posts_returns_list(self):
        posts = get_all_posts()
        assert isinstance(posts, list)

    def test_get_all_posts_has_100_items(self):
        posts = get_all_posts()
        assert len(posts) == 100

    def test_each_post_has_required_fields(self):
        posts = get_all_posts()
        for post in posts[:5]:  # check first 5
            assert "id" in post
            assert "title" in post
            assert "userId" in post


class TestCreatePost:
    """Tests for creating a post."""

    def test_create_post_returns_new_post(self):
        new_post = create_post("Test Title", "Test Body", 1)
        assert new_post["title"] == "Test Title"
        assert new_post["body"] == "Test Body"
        assert new_post["userId"] == 1

    def test_create_post_assigns_id(self):
        new_post = create_post("Another Test", "Body", 2)
        assert "id" in new_post
        assert new_post["id"] == 101  # JSONPlaceholder always returns 101