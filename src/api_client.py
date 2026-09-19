"""API client for testing JSONPlaceholder API.

Demonstrates how to test REST APIs using Python requests library.
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_post(post_id: int) -> dict:
    """Fetch a single post by ID.

    Args:
        post_id: The ID of the post to fetch.

    Returns:
        The post data as a dict.

    Raises:
        requests.HTTPError: If the request returns an error status.
    """
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
    response.raise_for_status()
    return response.json()


def get_all_posts() -> list:
    """Fetch all posts.

    Returns:
        A list of post dicts.
    """
    response = requests.get(f"{BASE_URL}/posts", timeout=10)
    response.raise_for_status()
    return response.json()


def get_post_status(post_id: int) -> int:
    """Return the HTTP status code for fetching a post.

    Args:
        post_id: The ID of the post to fetch.

    Returns:
        The HTTP status code (e.g., 200, 404).
    """
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
    return response.status_code


def create_post(title: str, body: str, user_id: int) -> dict:
    """Create a new post.

    Args:
        title: Post title.
        body: Post body.
        user_id: User ID to assign the post to.

    Returns:
        The created post as a dict.
    """
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Manual tests
    print("=== Get Post 1 ===")
    post = get_post(1)
    print(f"Title: {post['title'][:50]}...")

    print("\n=== Get Post 9999 (invalid) ===")
    status = get_post_status(9999)
    print(f"Status code: {status}")  # Should be 404

    print("\n=== Create Post ===")
    new_post = create_post("My Test Post", "Testing API", 1)
    print(f"Created post ID: {new_post['id']}")

    print("\n=== Get All Posts ===")
    posts = get_all_posts()
    print(f"Total posts: {len(posts)}")