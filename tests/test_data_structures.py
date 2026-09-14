"""Tests for src/collections.py."""

import pytest

from src.data_structures import (
    find_common_elements,
    get_average,
    unique_items,
    word_count,
)


class TestUniqueItems:
    """Tests for unique_items()."""

    def test_with_duplicates(self):
        assert unique_items([1,2,2,3,1]) == [1,2,3]
        pass

    def test_empty_list(self):
        assert unique_items([]) == []
        pass

    def test_preserves_order(self):
        assert unique_items([3,1,3,2,1]) == [3,1,2]
        pass


class TestWordCount:
    """Tests for word_count()."""

    def test_basic_count(self):
        result = word_count("the cat the dog")
        assert result == {"the": 2, "cat" : 1,"dog" : 1}
        pass

    def test_case_insensitive(self):
        assert word_count("The THE the") == {"the":3}
        pass

    def test_empty_string(self):
        assert word_count("") == {}
        pass


class TestFindCommonElements:
    """Tests for find_common_elements()."""

    def test_common_elements(self):
        assert find_common_elements([1,2,3],[2,3,4]) == {2,3}
        pass

    def test_no_common_elements(self):
        assert find_common_elements([1,2],[3,4]) == set()
        pass

    def test_empty_list(self):
        assert find_common_elements([],[1,2]) == set()
        pass


class TestGetAverage:
    """Tests for get_average()."""

    def test_normal_case(self):
        assert get_average([10,20,30]) == 20.0
        pass

    def test_single_number(self):
        assert get_average([5]) == 5.0
        pass

    def test_raises_on_empty_list(self):
        with pytest.raises(ValueError, match="numbers cannot be empty"):
            get_average([])
        pass