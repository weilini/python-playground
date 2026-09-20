"""Tests demonstrating pytest.mark.parametrize.

Parametrize lets you run the same test function
with multiple sets of inputs.
"""

import pytest

# ============================================================
# Example 1 — Basic parametrize
# ============================================================


def add(a: int, b: int) -> int:
    """Simple add function for testing."""
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
        (-5, -5, -10),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


# ============================================================
# Example 2 — Parametrize with strings
# ============================================================


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, ignores spaces)."""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("A man a plan a canal Panama", True),
        ("Was it a car or a cat I saw", True),
        ("hello", False),
        ("python", False),
        ("", True),
        ("a", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected


# ============================================================
# Example 3 — Testing error cases
# ============================================================


def safe_divide(a: float, b: float) -> float:
    """Divide a by b, raising ValueError if b is zero."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (7, 2, 3.5),
        (-10, 2, -5.0),
        (0, 5, 0.0),
    ],
)
def test_safe_divide_valid(a, b, expected):
    assert safe_divide(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        (10, 0),
        (0, 0),
        (-5, 0),
    ],
)
def test_safe_divide_by_zero_raises(a, b):
    with pytest.raises(ValueError, match="cannot divide by zero"):
        safe_divide(a, b)


# ============================================================
# Example 4 — Parametrize with ids (better test names)
# ============================================================


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-3, False),
        pytest.param(100, True, id="one_hundred"),
    ],
    ids=[
        "even_small",
        "odd_small",
        "zero",
        "even_negative",
        "odd_negative",
        "one_hundred",
    ],
)
def test_is_even(number, expected):
    assert (number % 2 == 0) == expected


# ============================================================
# Example 5 — Parametrize with a fixture
# ============================================================


@pytest.fixture
def multiplier():
    """Fixture that returns a multiplier function."""
    return lambda x: x * 2


@pytest.mark.parametrize(
    "input_value, expected",
    [
        (1, 2),
        (5, 10),
        (-3, -6),
        (0, 0),
    ],
)
def test_multiplier(multiplier, input_value, expected):
    assert multiplier(input_value) == expected


# ============================================================
# Example 6 — Multiple parametrize decorators (cartesian product)
# ============================================================


@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [10, 20])
def test_multiply(a, b):
    """This runs 3 × 2 = 6 times."""
    result = a * b
    assert result == a * b  # Always true, but shows the pattern
