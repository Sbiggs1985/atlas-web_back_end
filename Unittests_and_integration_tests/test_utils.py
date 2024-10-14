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
        """Method that returns what it is supposed to be."""
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


class TestGetJson(unittest.TestCase):
    """Test class for the utils.get_json function"""

    @patch('utils.requests.get')  # Mock requests.get
    def test_get_json(self, mock_get):
        """Test that get_json returns the expected result"""
        # Test cases: (URL, Payload)
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_cases:
            # Mock the .json() method on the return value of requests.get
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json and assert the result is as expected
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)  # Check requests.get
            self.assertEqual(result, test_payload)  # Check the result

            # Reset mock for the next iteration
            mock_get.reset_mock()


# If this script is executed directly, run the tests
if __name__ == '__main__':
    unittest.main()
