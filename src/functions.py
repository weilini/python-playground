"""Function exercises for Stage 2, Day 3.

This module demonstrates:
- Default arguments
- Keyword arguments
- *args and **kwargs
- Scope
- Modules and imports
"""


def format_name(first: str, last: str, middle: str = "") -> str:
    """Return a formatted full name.

    If middle is provided, include it between first and last.

    Args:
        first: First name.
        last: Last name.
        middle: Optional middle name (default: empty).

    Returns:
        A formatted full name.

    Examples:
        format_name("Lini", "Wei") -> "Lini Wei"
        format_name("Lini", "Wei", "Mary") -> "Lini Mary Wei"
    """
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

    



def sum_all(*numbers: float) -> float:
    """Return the sum of all numbers passed in.

    Args:
        *numbers: Any number of numeric values.

    Returns:
        The total sum. Returns 0 if no numbers are given.

    Examples:
        sum_all(1, 2, 3) -> 6
        sum_all() -> 0
    """
    return sum(numbers)


def build_profile(**info) -> dict:
    """Return a dictionary of the provided information.

    Args:
        **info: Any keyword arguments.

    Returns:
        The same dictionary, unchanged.

    Examples:
        build_profile(name="Lini", city="Cork")
        -> {"name": "Lini", "city": "Cork"}
    """
    return info




def apply_twice(func, value):
    """Apply a function to a value twice.

    Args:
        func: A function that takes one argument and returns a value.
        value: The initial value.

    Returns:
        The result of applying func twice.

    Example:
        apply_twice(lambda x: x + 1, 5) -> 7
    """
    return func(func(value))


def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius.

    This function demonstrates importing and using a function
    from another module (src.basics has celsius_to_fahrenheit).

    Formula: C = (F - 32) * 5/9

    Args:
        fahrenheit: Temperature in Fahrenheit.

    Returns:
        Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print(format_name("Lini", "Wei"))                    # Lini Wei
    print(format_name("Lini", "Wei", "Mary"))            # Lini Mary Wei
    print(sum_all(1, 2, 3, 4, 5))                        # 15
    print(sum_all())                                     # 0
    print(build_profile(name="Lini", city="Cork"))       # {'name': 'Lini', 'city': 'Cork'}
    print(apply_twice(lambda x: x * 2, 3))               # 12
    print(convert_to_celsius(32))                        # 0.0
    print(convert_to_celsius(212))                       # 100.0