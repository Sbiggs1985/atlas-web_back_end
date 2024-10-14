#!/usr/bin/env python3
"""Unittests for GithubOrgClient class"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that inherits from unittest.TestCase"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        # Mock the return value of get_json
        mock_get_json.return_value = {"org": org_name}

        client = GithubOrgClient(org_name)

        result = client.org()  # This should be callable

        url = f'https://api.github.com/orgs/{org_name}'

        mock_get_json.assert_called_once_with(url)

        self.assertEqual(result, {"name": org_name})


if __name__ == "__main__":
    unittest.main()
