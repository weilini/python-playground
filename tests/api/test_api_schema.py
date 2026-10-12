"""Tests that validate API responses against JSON Schemas.

Schema validation catches structural problems (missing fields, wrong
types) that value-based assertions miss.
"""

import jsonschema
import pytest
import responses

from src.api_client import (
    BASE_URL,
    POST_LIST_SCHEMA,
    POST_SCHEMA,
    get_all_posts,
    get_post,
)

# ---------------------------------------------------------------------------
# Valid responses pass schema validation
# ---------------------------------------------------------------------------


@responses.activate
def test_get_post_matches_schema() -> None:
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Hello", "body": "World", "userId": 1},
        status=200,
    )
    post = get_post(1)
    jsonschema.validate(instance=post, schema=POST_SCHEMA)


@responses.activate
def test_get_all_posts_matches_schema() -> None:
    responses.get(
        f"{BASE_URL}/posts",
        json=[
            {"id": 1, "title": "A", "body": "x", "userId": 1},
            {"id": 2, "title": "B", "body": "y", "userId": 2},
            {"id": 3, "title": "C", "body": "z", "userId": 1},
        ],
        status=200,
    )
    posts = get_all_posts()
    jsonschema.validate(instance=posts, schema=POST_LIST_SCHEMA)


# ---------------------------------------------------------------------------
# Invalid responses fail schema validation
# ---------------------------------------------------------------------------


@responses.activate
def test_post_missing_field_fails_schema() -> None:
    """Response missing `title` should fail validation."""
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "body": "World", "userId": 1},  # missing title
        status=200,
    )
    post = get_post(1)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=post, schema=POST_SCHEMA)


@responses.activate
def test_post_wrong_type_fails_schema() -> None:
    """`id` as a string should fail — schema requires integer."""
    responses.get(
        f"{BASE_URL}/posts/1",
        json={"id": "1", "title": "Hello", "body": "World", "userId": 1},
        status=200,
    )
    post = get_post(1)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=post, schema=POST_SCHEMA)


@responses.activate
def test_post_extra_field_fails_schema() -> None:
    """Extra field not in schema fails because additionalProperties=False."""
    responses.get(
        f"{BASE_URL}/posts/1",
        json={
            "id": 1,
            "title": "Hello",
            "body": "World",
            "userId": 1,
            "unexpected": "extra",
        },
        status=200,
    )
    post = get_post(1)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=post, schema=POST_SCHEMA)
