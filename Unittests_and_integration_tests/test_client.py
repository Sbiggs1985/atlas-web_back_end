#!/usr/bin/env python3
"""Unittests for GithubOrgClient class"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient  # Ensure to import your class correctly


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that inherits from unittest.TestCase"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')  # Ensure to patch the correct import path
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        mock_get_json.return_value = {"org": org_name}

        client = GithubOrgClient(org_name)

        result = client.org()

        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

        self.assertEqual(result, {"org": org_name})


if __name__ == "__main__":
    unittest.main()
