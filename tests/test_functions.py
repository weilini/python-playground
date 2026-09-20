"""Tests for src/functions.py."""

from src.functions import (
    apply_twice,
    build_profile,
    convert_to_celsius,
    format_name,
    sum_all,
)


class TestFormatName:
    """Tests for format_name()."""

    def test_first_and_last(self):
        assert format_name("Lini", "Wei") == "Lini Wei"

    def test_with_middle(self):
        assert format_name("Lini", "Wei", "Mary") == "Lini Mary Wei"

    def test_empty_middle(self):
        assert format_name("Lini", "Wei", "") == "Lini Wei"


class TestSumAll:
    """Tests for sum_all()."""

    def test_multiple_numbers(self):
        assert sum_all(1, 2, 3) == 6

    def test_no_numbers(self):
        assert sum_all() == 0

    def test_negative_numbers(self):
        assert sum_all(-1, -2, -3) == -6

    def test_mixed_numbers(self):
        assert sum_all(-1, 0, 1) == 0


class TestBuildProfile:
    """Tests for build_profile()."""

    def test_two_fields(self):
        result = build_profile(name="Lini", city="Cork")
        assert result == {"name": "Lini", "city": "Cork"}

    def test_no_fields(self):
        assert build_profile() == {}


class TestApplyTwice:
    """Tests for apply_twice()."""

    def test_double(self):
        assert apply_twice(lambda x: x * 2, 3) == 12

    def test_increment(self):
        assert apply_twice(lambda x: x + 1, 5) == 7


class TestConvertToCelsius:
    """Tests for convert_to_celsius()."""

    def test_freezing(self):
        assert convert_to_celsius(32) == 0.0

    def test_boiling(self):
        assert convert_to_celsius(212) == 100.0

    def test_negative_forty(self):
        assert convert_to_celsius(-40) == -40.0
