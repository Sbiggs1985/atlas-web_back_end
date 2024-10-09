#!/usr/bin/env python3
"""Unittests and integration tests"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json, access_nested_map, memoize
import requests


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from unittest.TestCase!"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])


    def test_access_nested_map(self, nested_map, path, expected):
        """Method that returns whaat it is supposed to be."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),               # Empty dict, "a" key missing
        ({"a": 1}, ("a", "b")),     # Key "b" missing in nested dict
    ])


    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised when the path is not found."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{path[-1]}'")

    if __name__ == "__main__":
        unittest.main()
