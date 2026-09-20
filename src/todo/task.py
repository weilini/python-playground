"""Task class representing a single to-do item."""

from dataclasses import asdict, dataclass


@dataclass
class Task:
    """A single to-do task.

    Attributes:
        title: Description of the task.
        done: Whether the task is completed.
    """

    title: str
    done: bool = False

    def __str__(self) -> str:
        """Return a human-readable representation."""
        status = "✓" if self.done else " "
        return f"[{status}] {self.title}"

    def to_dict(self) -> dict:
        """Convert to a JSON-serializable dict."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task from a dict."""
        return cls(title=data["title"], done=data.get("done", False))
