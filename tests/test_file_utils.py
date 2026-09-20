"""Tests for src/utils/file_utils.py."""

from src.utils.file_utils import append_line, count_lines


class TestAppendLine:
    def test_creates_file(self, tmp_path):
        file = tmp_path / "test.txt"
        append_line(str(file), "hello")
        assert file.read_text() == "hello\n"

    def test_appends_to_existing(self, tmp_path):
        file = tmp_path / "test.txt"
        append_line(str(file), "line 1")
        append_line(str(file), "line 2")
        assert file.read_text() == "line 1\nline 2\n"


class TestCountLines:
    def test_empty_file(self, tmp_path):
        file = tmp_path / "empty.txt"
        file.write_text("")
        assert count_lines(str(file)) == 0

    def test_one_line(self, tmp_path):
        file = tmp_path / "one.txt"
        file.write_text("hello\n")
        assert count_lines(str(file)) == 1

    def test_multiple_lines(self, tmp_path):
        file = tmp_path / "multi.txt"
        file.write_text("line 1\nline 2\nline 3\n")
        assert count_lines(str(file)) == 3
