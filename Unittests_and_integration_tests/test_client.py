#!/usr/bin/env python3
"""Unittests and integration tests"""

import unittest
from unittest.mock import patch, Mock
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test class for utils.get_json function."""

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test get_json with mocked requests.get."""
        # Test cases with test_url and test_payload
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Configure the mock to return a response with the test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json and check the result
            result = get_json(test_url)

            # Ensure that requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)

            # Check that the output of get_json is equal to test_payload
            self.assertEqual(result, test_payload)

            # Reset mock to ensure clean slate for the next test case
            mock_get.reset_mock()


if __name__ == "__main__":
    unittest.main()
