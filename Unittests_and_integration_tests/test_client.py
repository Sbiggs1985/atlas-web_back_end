#!/usr/bin/env python3
"""Unittests and integration tests"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)

        result = client.org()

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, {"login": org_name})


if __name__ == "__main__":
    unittest.main()
