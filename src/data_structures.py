"""Collection exercises for Stage 2, Day 2.

This module demonstrates:
- Lists
- Dictionaries
- Sets
- Tuples
- Comprehensions
"""


def unique_items(items: list) -> list:
    """Return a list of unique items, preserving order.

    Args:
        items: A list that may contain duplicates.

    Returns:
        A list with duplicates removed, in original order.

    Example:
        unique_items([1, 2, 2, 3, 1]) -> [1, 2, 3]
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def word_count(text: str) -> dict:
    """Count how many times each word appears in a text.

    Words are case-insensitive. Ignore empty strings.

    Args:
        text: A string of words.

    Returns:
        A dict mapping each lowercase word to its count.

    Example:
        word_count("the cat the dog") -> {"the": 2, "cat": 1, "dog": 1}
    """
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def find_common_elements(list1: list, list2: list) -> set:
    """Return the set of elements that appear in both lists.

    Args:
        list1: First list.
        list2: Second list.

    Returns:
        A set of common elements.

    Example:
        find_common_elements([1, 2, 3], [2, 3, 4]) -> {2, 3}
    """
    return set(list1) & set(list2)


def get_average(numbers: list) -> float:
    """Return the average (mean) of a list of numbers.

    Args:
        numbers: A list of ints or floats.

    Returns:
        The average as a float.

    Raises:
        ValueError: If the list is empty.

    Example:
        get_average([10, 20, 30]) -> 20.0
    """
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)

    pass


if __name__ == "__main__":
    # Manual test — run this file to see output
    print(unique_items([1, 2, 2, 3, 1]))  # [1, 2, 3]
    print(word_count("the cat the dog"))  # {'the': 2, 'cat': 1, 'dog': 1}
    print(find_common_elements([1, 2, 3], [2, 3, 4]))  # {2, 3}
    print(get_average([10, 20, 30]))  # 20.0
