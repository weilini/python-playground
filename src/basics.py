"""Basic Python functions for Stage 2, Day 1.

This module demonstrates:
- Variables and types
- Arithmetic operators
- f-strings
- Function definitions with type hints
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Formula: F = C * 9/5 + 32

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.
    """
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def calculate_age(birth_year: int, current_year: int) -> int:
    """Calculate age given a birth year and a current year.

    Args:
        birth_year: The year the person was born.
        current_year: The current year.

    Returns:
        Age in years.

    Raises:
        ValueError: If birth_year is after current_year.
    """
    if birth_year > current_year:
        raise ValueError("birth_year cannot be after current_year")

    age = current_year - birth_year
    return age


def greet_user(name: str, city: str) -> str:
    """Return a friendly greeting combining name and city.

    Args:
        name: The user's first name.
        city: The city they live in.

    Returns:
        A greeting string.
    """
    greeting = f"Hello, {name} from {city}!"
    return greeting


if __name__ == "__main__":
    # Manual test — run this file directly to see output
    print(celsius_to_fahrenheit(0))      # 32.0
    print(celsius_to_fahrenheit(100))    # 212.0
    print(calculate_age(1990, 2026))     # 36
    print(greet_user("Lini", "Cork"))    # Hello, Lini from Cork!