#!/usr/bin/env python3
"""Parameterize
"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Tests the AccessNestedMap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_res: Union[Dict, int],
            ) -> None:
        """Test output"""
        self.assertEqual(access_nested_map(nested_map, path), expected_res)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Test exceptions"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests Json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests Json outputs."""
        dicts = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**dicts)) as res_get:
            self.assertEqual(get_json(test_url), test_payload)
            res_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test memoize class"""
    def test_memoize(self) -> None:
        """Test output"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo:
            class_test = TestClass()
            self.assertEqual(class_test.a_property(), 42)
            self.assertEqual(class_test.a_property(), 42)
            memo.assert_called_once()
