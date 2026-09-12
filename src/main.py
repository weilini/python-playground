"""Entry point for the Python Playground."""


def greet(name: str) -> str:
    """Return a friendly greeting.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string.

    Raises:
        ValueError: If name is empty.
    """
    if not name:
        raise ValueError("name cannot be empty")
    return f"Hello, {name}! Welcome to your Python journey."


if __name__ == "__main__":
    print(greet("Lini"))