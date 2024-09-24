#!/usr/bin/env python3
"""Unittests and integration tests"""

import unittest
from unittest.mock import patch, Mock
from utils import get_json


class TestGetJson(unittest.TestCase):
    """TestGetJson class that tests utils.get_json"""

    @patch('utils.requests.get')  # Patching requests.get
    def test_get_json_example_com(self, mock_get):
        """Test get_json with 'http://example.com' and a mocked payload"""
        test_url = "http://example.com"
        test_payload = {"payload": True}

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)

    @patch('utils.requests.get')  # Patching requests.get
    def test_get_json_holberton_io(self, mock_get):
        """Test get_json with 'http://holberton.io' and a mocked payload"""
        test_url = "http://holberton.io"
        test_payload = {"payload": False}

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
