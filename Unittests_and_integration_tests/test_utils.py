#!/usr/bin/env python3
"""Unittests and integration tests"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from unittest.TestCase!"""
    @parameterized.expand([
        # parameterized.expand is the decorator
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])


    def test_access_nested_map(self, nested_map, path, expected):
        """Method that returns whaat it is supposed to be."""
        self.assertEqual(access_nested_map(nested_map, path) expected)


if __name__ == "__main__":
    unittest.main()
