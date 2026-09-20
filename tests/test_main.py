"""Tests for src/main.py."""

import pytest

from src.main import greet


def test_greet_returns_expected_message():
    """greet() returns the expected message for a normal name."""
    assert greet("Lini") == "Hello, Lini! Welcome to your Python journey."


def test_greet_raises_on_empty_name():
    """greet() raises ValueError when given an empty name."""
    with pytest.raises(ValueError, match="name cannot be empty"):
        greet("")
