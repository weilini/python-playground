"""Tests for src/api_client.py — JSONPlaceholder API tests."""

from src.api_client import (
    create_post,
    delete_post,
    get_all_posts,
    get_post,
    get_post_status,
    update_post,
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
        for post in posts[:5]:
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
        assert new_post["id"] == 101


class TestUpdatePost:
    """Tests for updating a post."""

    def test_update_post_returns_updated_data(self):
        updated = update_post(1, "Updated Title", "Updated Body", 1)
        assert updated["title"] == "Updated Title"
        assert updated["body"] == "Updated Body"


class TestDeletePost:
    """Tests for deleting a post."""

    def test_delete_post_returns_200(self):
        assert delete_post(1) == 200
