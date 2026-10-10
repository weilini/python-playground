"""API client for testing JSONPlaceholder API.

Demonstrates how to test REST APIs using Python requests library.
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_post(post_id: int) -> dict:
    """Fetch a single post by ID."""
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
    response.raise_for_status()
    return response.json()


def get_all_posts() -> list:
    """Fetch all posts."""
    response = requests.get(f"{BASE_URL}/posts", timeout=10)
    response.raise_for_status()
    return response.json()


def get_post_status(post_id: int) -> int:
    """Return the HTTP status code for fetching a post."""
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
    return response.status_code


def create_post(title: str, body: str, user_id: int) -> dict:
    """Create a new post."""
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


def update_post(post_id: int, title: str, body: str, user_id: int) -> dict:
    """Update an existing post (PUT)."""
    payload = {"id": post_id, "title": title, "body": body, "userId": user_id}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


def delete_post(post_id: int) -> int:
    """Delete a post (DELETE). Returns status code."""
    response = requests.delete(f"{BASE_URL}/posts/{post_id}", timeout=10)
    return response.status_code


# ---------------------------------------------------------------------------
# Authenticated requests
# ---------------------------------------------------------------------------


def get_protected_resource(token: str) -> dict:
    """Fetch a protected resource using Bearer token auth.

    Sends: Authorization: Bearer <token>
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/posts/1", headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def get_with_basic_auth(username: str, password: str) -> dict:
    """Fetch using HTTP Basic Auth.

    `requests` handles the base64 encoding automatically.
    """
    response = requests.get(
        f"{BASE_URL}/posts/1",
        auth=(username, password),
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def get_with_custom_headers(headers: dict) -> dict:
    """Fetch with arbitrary custom headers (e.g. X-API-Key, User-Agent)."""
    response = requests.get(
        f"{BASE_URL}/posts/1",
        headers=headers,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("=== Get Post 1 ===")
    print(f"Title: {get_post(1)['title'][:50]}...")
    print("\n=== Get Post 9999 (invalid) ===")
    print(f"Status code: {get_post_status(9999)}")
    print("\n=== Create Post ===")
    print(f"Created post ID: {create_post('My Test Post', 'Testing API', 1)['id']}")
    print("\n=== Get All Posts ===")
    print(f"Total posts: {len(get_all_posts())}")
    print("\n=== Update Post ===")
    print(
        f"Updated title: {update_post(1, 'Updated Title', 'Updated Body', 1)['title']}"
    )
    print("\n=== Delete Post ===")
    print(f"Delete status: {delete_post(1)}")
