"""Entry point for `python -m src.todo`."""

import sys

from src.todo.cli import main

if __name__ == "__main__":
    sys.exit(main())
