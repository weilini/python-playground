"""Command-line interface for the To-Do app."""

import sys

from src.todo.todo_list import TodoList


def print_usage() -> None:
    """Print usage instructions."""
    print("Usage: python -m src.todo <command> [args]")
    print()
    print("Commands:")
    print('  add "Task title"    Add a new task')
    print("  list                Show all tasks")
    print("  complete N          Mark task N as done")
    print("  delete N            Delete task N")
    print("  clear               Delete all tasks")


def cmd_add(todo: TodoList, args: list[str]) -> None:
    if not args:
        print("Error: 'add' requires a task title.")
        return
    title = " ".join(args)
    try:
        task = todo.add(title)
        print(f"Added: {task}")
    except ValueError as e:
        print(f"Error: {e}")


def cmd_list(todo: TodoList) -> None:
    tasks = todo.all()
    if not tasks:
        print('No tasks. Add one with: add "Task title"')
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def cmd_complete(todo: TodoList, args: list[str]) -> None:
    if not args or not args[0].isdigit():
        print("Error: 'complete' requires a task number.")
        return
    try:
        task = todo.complete(int(args[0]))
        print(f"Completed: {task}")
    except IndexError as e:
        print(f"Error: {e}")


def cmd_delete(todo: TodoList, args: list[str]) -> None:
    if not args or not args[0].isdigit():
        print("Error: 'delete' requires a task number.")
        return
    try:
        task = todo.delete(int(args[0]))
        print(f"Deleted: {task}")
    except IndexError as e:
        print(f"Error: {e}")


def cmd_clear(todo: TodoList) -> None:
    todo.clear()
    print("All tasks cleared.")


def main(argv: list[str] | None = None) -> int:
    """Entry point for the CLI.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    argv = argv if argv is not None else sys.argv[1:]

    if not argv:
        print_usage()
        return 0

    command = argv[0]
    args = argv[1:]
    todo = TodoList()

    if command == "add":
        cmd_add(todo, args)
    elif command == "list":
        cmd_list(todo)
    elif command == "complete":
        cmd_complete(todo, args)
    elif command == "delete":
        cmd_delete(todo, args)
    elif command == "clear":
        cmd_clear(todo)
    else:
        print(f"Unknown command: {command}")
        print_usage()
        return 1

    return 0
