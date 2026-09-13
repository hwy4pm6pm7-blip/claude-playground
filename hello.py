"""A tiny utility module with a couple of pure functions."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def greet(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))
    print(f"2 + 3 = {add(2, 3)}")
