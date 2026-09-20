"""Mathematical utility functions."""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a times b."""
    return a * b


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    is_even = n % 2 == 0
    return is_even


if __name__ == "__main__":
    print(add(2, 3))  # 5
    print(subtract(10, 4))  # 6
    print(multiply(3, 4))  # 12
    print(is_even(4))  # True
    print(is_even(7))  # False
