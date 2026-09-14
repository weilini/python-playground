"""Tests for src/file_io.py."""

import json

import pytest

from src.file_io import (
    load_json,
    read_text,
    safe_divide,
    save_json,
    write_text,
)


class TestWriteAndReadText:
    """Tests for write_text() and read_text()."""

    def test_write_then_read(self, tmp_path):
        file = tmp_path / "test.txt"
        write_text(str(file), "hello")
        assert read_text(str(file)) == "hello"

    def test_overwrites_existing_file(self, tmp_path):
        file = tmp_path / "test.txt"
        write_text(str(file), "first")
        write_text(str(file), "second")
        assert read_text(str(file)) == "second"

    def test_read_missing_file_raises(self, tmp_path):
        missing = tmp_path / "missing.txt"
        with pytest.raises(FileNotFoundError):
            read_text(str(missing))


class TestSaveAndLoadJson:
    """Tests for save_json() and load_json()."""

    def test_save_then_load(self, tmp_path):
        file = tmp_path / "user.json"
        data = {"name": "Lini", "age": 36}
        save_json(str(file), data)
        assert load_json(str(file)) == data

    def test_load_invalid_json_raises(self, tmp_path):
        file = tmp_path / "bad.json"
        file.write_text("not valid json {{{")
        with pytest.raises(json.JSONDecodeError):
            load_json(str(file))


class TestSafeDivide:
    """Tests for safe_divide()."""

    def test_normal_division(self):
        assert safe_divide(10, 2) == 5.0

    def test_float_division(self):
        assert safe_divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="cannot divide by zero"):
            safe_divide(10, 0)