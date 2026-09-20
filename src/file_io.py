"""File I/O and error handling exercises for Stage 2, Day 4.

This module demonstrates:
- Reading and writing text files
- JSON serialization
- Error handling with try/except
- Context managers (with statement)
"""

import json


def write_text(filename: str, content: str) -> None:
    """Write text content to a file, overwriting if it exists.

    Args:
        filename: Path to the file to write.
        content: Text content to write.
    """
    with open(filename, "w") as f:
        f.write(content)


def read_text(filename: str) -> str:
    """Read and return the contents of a text file.

    Args:
        filename: Path to the file to read.

    Returns:
        The full contents of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(filename) as f:
        return f.read()


def save_json(filename: str, data: dict) -> None:
    """Save a dictionary to a file as pretty-printed JSON.

    Args:
        filename: Path to the file to write.
        data: Dictionary to serialize.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_json(filename: str) -> dict:
    """Load a dictionary from a JSON file.

    Args:
        filename: Path to the JSON file.

    Returns:
        The parsed JSON as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    with open(filename) as f:
        return json.load(f)


def safe_divide(a: float, b: float) -> float:
    """Divide a by b, raising ValueError if b is zero.

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    with open("division.log", "a"):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


if __name__ == "__main__":
    # Manual tests — these will create files in the current directory
    write_text("/tmp/test_notes.txt", "Hello, world!")
    print(read_text("/tmp/test_notes.txt"))

    save_json("/tmp/test_user.json", {"name": "Lini", "city": "Cork"})
    print(load_json("/tmp/test_user.json"))

    print(safe_divide(10, 2))
    # print(safe_divide(10, 0))  # Uncomment to test the error path
