"""Tests for src/decorators.py."""

from src.decorators import count_calls, log_calls, shout


class TestShout:
    """Tests for the @shout decorator."""

    def test_uppercases_result(self):
        @shout
        def greet():
            return "hello"

        assert greet() == "HELLO"

    def test_works_with_arguments(self):
        @shout
        def greet(name):
            return f"hello {name}"

        assert greet("lini") == "HELLO LINI"

    def test_preserves_name(self):
        @shout
        def greet():
            return "hello"

        assert greet.__name__ == "greet"


class TestLogCalls:
    """Tests for the @log_calls decorator."""

    def test_prints_before_and_after(self, capsys):
        @log_calls
        def add(a, b):
            return a + b

        add(2, 3)
        captured = capsys.readouterr()
        assert "Calling add" in captured.out
        assert "add returned 5" in captured.out

    def test_returns_original_result(self):
        @log_calls
        def add(a, b):
            return a + b

        assert add(2, 3) == 5


class TestCountCalls:
    """Tests for the @count_calls decorator."""

    def test_starts_at_zero(self):
        @count_calls
        def ping():
            return "pong"

        assert ping.call_count == 0

    def test_increments_per_call(self):
        @count_calls
        def ping():
            return "pong"

        ping()
        ping()
        ping()
        assert ping.call_count == 3

    def test_returns_original_result(self):
        @count_calls
        def ping():
            return "pong"

        result = ping()
        assert result == "pong"
