"""Tests for src/basics.py."""

import pytest

from src.basics import calculate_age, celsius_to_fahrenheit, greet_user


class TestCelsiusToFahrenheit:
    """Tests for celsius_to_fahrenheit()."""

    def test_freezing_point(self):
        assert celsius_to_fahrenheit(0) == 32.0

    def test_boiling_point(self):
        assert celsius_to_fahrenheit(100) == 212.0

    def test_negative_forty(self):
        # -40°C equals -40°F — a famous coincidence
        assert celsius_to_fahrenheit(-40) == -40.0

    def test_room_temperature(self):
        assert celsius_to_fahrenheit(20) == 68.0


class TestCalculateAge:
    """Tests for calculate_age()."""

    def test_normal_case(self):
        assert calculate_age(1990, 2026) == 36

    def test_newborn(self):
        assert calculate_age(2026, 2026) == 0

    def test_one_year_old(self):
        assert calculate_age(2025, 2026) == 1

    def test_raises_on_future_birth_year(self):
        with pytest.raises(ValueError, match="birth_year cannot be after current_year"):
            calculate_age(2030, 2026)


class TestGreetUser:
    """Tests for greet_user()."""

    def test_normal_greeting(self):
        assert greet_user("Lini", "Cork") == "Hello, Lini from Cork!"

    def test_different_name_and_city(self):
        assert greet_user("Alice", "Dublin") == "Hello, Alice from Dublin!"

    def test_empty_name_still_produces_greeting(self):
        # We allow empty name for now — just checking behaviour
        assert greet_user("", "Cork") == "Hello,  from Cork!"