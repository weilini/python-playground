"""Decorator exercises for Stage 2, Day 8.

This module demonstrates:
- Functions as objects
- Writing decorators
- The @decorator syntax
- functools.wraps
"""

import functools


def shout(func):
    """Decorator that uppercases the string result of a function.

    Example:
        @shout
        def greet():
            return "hello"

        greet()  # "HELLO"
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def log_calls(func):
    """Decorator that prints before and after calling the function.

    Example:
        @log_calls
        def add(a, b):
            return a + b

        add(2, 3)
        # Prints: Calling add(2, 3)
        #         add returned 5
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


def count_calls(func):
    """Decorator that counts how many times the function is called.

    The count is stored on the wrapper as .call_count.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


if __name__ == "__main__":
    @shout
    def greet():
        return "hello"

    print(greet())          # "HELLO"

    @log_calls
    def add(a, b):
        return a + b

    add(2, 3)
    # Calling add(2, 3)
    # add returned 5

    @count_calls
    def ping():
        return "pong"

    ping()
    ping()
    ping()
    print(ping.call_count)  # 3