#!/usr/bin/env python3
"""test a client"""
import unittest
from typing import Dict
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test github client"""
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, orgs_name: str, repres: Dict, magic: MagicMock) -> None:
        """test org"""
        magic.return_value = MagicMock(return_value=repres)
        git_org = GithubOrgClient(orgs_name)
        self.assertEqual(git_org.org(), repres)
        magic.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(orgs_name)
        )

    def test_public_repos_url(self) -> None:
        """test public repo url"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock:
            mock.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
