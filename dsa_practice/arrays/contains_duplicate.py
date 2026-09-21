"""LeetCode 217 — Contains Duplicate (Easy).

Problem:
    Given an integer array `nums`, return True if any value appears
    at least twice. Return False if all elements are distinct.

Examples:
    [1, 2, 3, 1] -> True
    [1, 2, 3, 4] -> False
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True
"""


def contains_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums)


def test_contains_duplicate_has_duplicates() -> None:
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_contains_duplicate_all_unique() -> None:
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_contains_duplicate_many_duplicates() -> None:
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_contains_duplicate_single_element() -> None:
    assert contains_duplicate([1]) is False


def test_contains_duplicate_two_same() -> None:
    assert contains_duplicate([1, 1]) is True


def test_contains_duplicate_negative_numbers() -> None:
    assert contains_duplicate([-1, -2, -3, -1]) is True
    # return True if the length of the set of nums is less than the length of nums
