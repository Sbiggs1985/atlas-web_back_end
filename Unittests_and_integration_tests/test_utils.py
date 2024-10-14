#!/usr/bin/env python3
"""Unittests for utils module"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json, access_nested_map, memoize
import requests

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function."""
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Check that requests.get was called correctly
        mock_get.assert_called_once_with(test_url)

        # Check the result is as expected
        self.assertEqual(result, test_payload)

if __name__ == "__main__":
    unittest.main()
