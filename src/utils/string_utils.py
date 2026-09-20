"""String manipulation utilities."""


def capitalize_words(text: str) -> str:
    """Return the text with each word capitalized.

    Example: "hello world" -> "Hello World"
    """
    return text.title()


def count_words(text: str) -> int:
    """Return the number of words in the text.

    Example: "hello world" -> 2
    """
    return len(text.split())


def reverse(text: str) -> str:
    """Return the text reversed.

    Example: "hello" -> "olleh"
    """
    return text[::-1]


if __name__ == "__main__":
    print(capitalize_words("hello world"))  # Hello World
    print(count_words("hello world foo"))  # 3
    print(reverse("hello"))  # olleh
