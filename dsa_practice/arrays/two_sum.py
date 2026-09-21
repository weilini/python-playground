"""LeetCode 1 — Two Sum (Easy)."""


def two_sum_brute(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    raise ValueError("No solution")


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    raise ValueError("No solution")


def test_two_sum_basic() -> None:
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_three_elements() -> None:
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_two_sum_duplicates() -> None:
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_negative_numbers() -> None:
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
