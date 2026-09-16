"""File utility functions.

This module demonstrates importing from another module in the project.
"""

from src.file_io import read_text, write_text


def append_line(filename: str, line: str) -> None:
    """Append a line to a file, creating it if it doesn't exist.

    Args:
        filename: Path to the file.
        line: Text to append. A newline is added automatically.
    """
    try:
        existing = read_text(filename)
    except FileNotFoundError:
        existing = ""
    write_text(filename, existing + line + "\n")


def count_lines(filename: str) -> int:
    """Return the number of lines in a file.

    Args:
        filename: Path to the file.

    Returns:
        Number of lines (empty lines count as lines).
    """
    content = read_text(filename)
    if not content:
        return 0
    return len(content.splitlines())


if __name__ == "__main__":
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmpdir:
        file = Path(tmpdir) / "test.txt"
        append_line(str(file), "First line")
        append_line(str(file), "Second line")
        print(count_lines(str(file)))    # 2