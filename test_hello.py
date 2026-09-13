"""Unit tests for hello.py."""

import unittest

from hello import add, greet


class HelloTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_greet(self):
        self.assertEqual(greet("world"), "Hello, world!")
        self.assertEqual(greet("Claude"), "Hello, Claude!")


if __name__ == "__main__":
    unittest.main()
