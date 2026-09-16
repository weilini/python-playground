"""Tests for src/todo/."""

import json

import pytest

from src.todo.task import Task
from src.todo.todo_list import TodoList


class TestTask:
    """Tests for the Task dataclass."""

    def test_new_task_is_not_done(self):
        task = Task(title="Buy milk")
        assert task.done is False

    def test_str_pending(self):
        task = Task(title="Buy milk")
        assert str(task) == "[ ] Buy milk"

    def test_str_done(self):
        task = Task(title="Buy milk", done=True)
        assert str(task) == "[✓] Buy milk"

    def test_to_dict(self):
        task = Task(title="Test", done=True)
        assert task.to_dict() == {"title": "Test", "done": True}

    def test_from_dict(self):
        task = Task.from_dict({"title": "Test", "done": True})
        assert task.title == "Test"
        assert task.done is True


class TestTodoList:
    """Tests for the TodoList class."""

    def test_starts_empty(self, tmp_path):
        todo = TodoList(path=str(tmp_path / "todo.json"))
        assert todo.all() == []

    def test_add_task(self, tmp_path):
        todo = TodoList(path=str(tmp_path / "todo.json"))
        todo.add("Buy milk")
        assert len(todo.all()) == 1
        assert todo.all()[0].title == "Buy milk"

    def test_add_empty_title_raises(self, tmp_path):
        todo = TodoList(path=str(tmp_path / "todo.json"))
        with pytest.raises(ValueError, match="cannot be empty"):
            todo.add("   ")

    def test_complete_task(self, tmp_path):
        todo = TodoList(path=str(tmp_path / "todo.json"))
        todo.add("Buy milk")
        task = todo.complete(1)
        assert task.done is True

    def test_complete_out_of_range_raises(self, tmp_path):
        todo = TodoList(path=str(tmp_path / "todo.json"))
        with pytest.raises(IndexError, match="does not exist"):
            todo.complete(1)

    def test_delete_task(self, tmp_path):
        todo = TodoList(path=str(tmp_path / "todo.json"))
        todo.add("Task 1")
        todo.add("Task 2")
        todo.delete(1)
        assert len(todo.all()) == 1
        assert todo.all()[0].title == "Task 2"

    def test_delete_out_of_range_raises(self, tmp_path):
        todo = TodoList(path=str(tmp_path / "todo.json"))
        with pytest.raises(IndexError):
            todo.delete(5)

    def test_clear_removes_all(self, tmp_path):
        todo = TodoList(path=str(tmp_path / "todo.json"))
        todo.add("Task 1")
        todo.add("Task 2")
        todo.clear()
        assert todo.all() == []

    def test_persistence(self, tmp_path):
        path = str(tmp_path / "todo.json")
        todo1 = TodoList(path=path)
        todo1.add("Buy milk")
        todo1.add("Write tests")
        todo1.complete(1)

        todo2 = TodoList(path=path)
        tasks = todo2.all()
        assert len(tasks) == 2
        assert tasks[0].title == "Buy milk"
        assert tasks[0].done is True
        assert tasks[1].title == "Write tests"
        assert tasks[1].done is False

    def test_corrupt_json_starts_fresh(self, tmp_path):
        path = tmp_path / "todo.json"
        path.write_text("not valid json {{{")
        todo = TodoList(path=str(path))
        assert todo.all() == []