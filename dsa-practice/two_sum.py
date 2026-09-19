"""LeetCode 1: Two Sum

Given an array of integers and a target, return indices of the
two numbers that add up to the target.

Example:
    nums = [2, 7, 11, 15], target = 9
    → [0, 1]  (because 2 + 7 = 9)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers that sum to target.

    Args:
        nums: List of integers.
        target: Target sum.

    Returns:
        List of two indices [i, j].

    Raises:
        ValueError: If no solution exists.
    """
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    raise ValueError("No solution")


if __name__ == "__main__":
    # Test cases
    print(two_sum([2, 7, 11, 15], 9))    # [0, 1]
    print(two_sum([3, 2, 4], 6))          # [1, 2]
    print(two_sum([3, 3], 6))             # [0, 1]