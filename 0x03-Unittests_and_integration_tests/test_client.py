#!/usr/bin/env python3
"""test a client"""
import unittest
from typing import Dict
from parameterized import parameterized
from unittest.mock import patch, MagicMock
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
