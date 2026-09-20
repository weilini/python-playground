"""Tests for src/utils/string_utils.py."""

from src.utils.string_utils import capitalize_words, count_words, reverse


class TestCapitalizeWords:
    def test_single_word(self):
        assert capitalize_words("hello") == "Hello"

    def test_multiple_words(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_empty_string(self):
        assert capitalize_words("") == ""


class TestCountWords:
    def test_two_words(self):
        assert count_words("hello world") == 2

    def test_single_word(self):
        assert count_words("hello") == 1

    def test_empty_string(self):
        assert count_words("") == 0


class TestReverse:
    def test_basic(self):
        assert reverse("hello") == "olleh"

    def test_palindrome(self):
        assert reverse("racecar") == "racecar"

    def test_empty_string(self):
        assert reverse("") == ""
