"""TodoList — manages a collection of tasks and persists to JSON."""

import json
from pathlib import Path

from src.todo.task import Task


class TodoList:
    """A collection of tasks with JSON persistence.

    Attributes:
        tasks: List of Task objects.
        path: Path to the JSON file (default ~/.todo.json).
    """

    def __init__(self, path: str | None = None):
        """Create a TodoList. Loads existing tasks if the file exists."""
        self.path = Path(path) if path else Path.home() / ".todo.json"
        self.tasks: list[Task] = []
        self._load()

    def _load(self) -> None:
        """Load tasks from the JSON file if it exists."""
        if not self.path.exists():
            return
        try:
            with open(self.path) as f:
                data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            # Corrupt file — start fresh
            self.tasks = []

    def save(self) -> None:
        """Save tasks to the JSON file."""
        with open(self.path, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def add(self, title: str) -> Task:
        """Add a new task. Returns the created Task."""
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = Task(title=title)
        self.tasks.append(task)
        self.save()
        return task

    def complete(self, index: int) -> Task:
        """Mark the task at the given 1-based index as done.

        Raises:
            IndexError: If the index is out of range.
        """
        task = self._get_task(index)
        task.done = True
        self.save()
        return task

    def delete(self, index: int) -> Task:
        """Delete the task at the given 1-based index.

        Raises:
            IndexError: If the index is out of range.
        """
        task = self._get_task(index)
        self.tasks.remove(task)
        self.save()
        return task

    def clear(self) -> None:
        """Delete all tasks."""
        self.tasks = []
        self.save()

    def all(self) -> list[Task]:
        """Return a copy of all tasks."""
        return list(self.tasks)

    def _get_task(self, index: int) -> Task:
        """Get task by 1-based index. Raises IndexError if out of range."""
        if index < 1 or index > len(self.tasks):
            raise IndexError(f"Task {index} does not exist.")
        return self.tasks[index - 1]
