"""Tests for src/utils/math_utils.py."""

from src.utils.math_utils import add, is_even, multiply, subtract


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_normal(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 10) == -7


class TestMultiply:
    def test_normal(self):
        assert multiply(3, 4) == 12

    def test_zero(self):
        assert multiply(5, 0) == 0


class TestIsEven:
    def test_even(self):
        assert is_even(4) is True

    def test_odd(self):
        assert is_even(7) is False

    def test_zero(self):
        assert is_even(0) is True
