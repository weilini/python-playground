"""Tests demonstrating pytest fixtures.

Fixtures are functions that provide test data or setup.
"""

import pytest


# ============================================================
# Simple fixture — returns a value
# ============================================================


@pytest.fixture
def sample_user():
    """Provide a sample user dict for tests."""
    return {"name": "Lini", "age": 36, "city": "Cork"}


def test_user_has_name(sample_user):
    assert sample_user["name"] == "Lini"


def test_user_has_age(sample_user):
    assert sample_user["age"] == 36


def test_user_has_city(sample_user):
    assert sample_user["city"] == "Cork"


# ============================================================
# Fixture with multiple values
# ============================================================


@pytest.fixture
def sample_numbers():
    """Provide a list of numbers."""
    return [1, 2, 3, 4, 5]


def test_sum(sample_numbers):
    assert sum(sample_numbers) == 15


def test_length(sample_numbers):
    assert len(sample_numbers) == 5


def test_max(sample_numbers):
    assert max(sample_numbers) == 5


# ============================================================
# Fixture using another fixture
# ============================================================


@pytest.fixture
def user_with_greeting(sample_user):
    """Provide a user with a pre-built greeting."""
    return {
        **sample_user,
        "greeting": f"Hello, {sample_user['name']}!",
    }


def test_greeting(user_with_greeting):
    assert user_with_greeting["greeting"] == "Hello, Lini!"


# ============================================================
# Fixture with setup and teardown (yield)
# ============================================================


@pytest.fixture
def temporary_list():
    """Provide a list that gets cleaned up after the test."""
    items = []
    yield items
    # This runs AFTER the test
    items.clear()


def test_add_to_list(temporary_list):
    temporary_list.append("item")
    assert len(temporary_list) == 1


def test_list_is_clean(temporary_list):
    # Each test gets a FRESH list
    assert len(temporary_list) == 0
