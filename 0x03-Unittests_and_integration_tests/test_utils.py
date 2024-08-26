#!/usr/bin/env python3
""" module doc"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ testing access_nested_map class """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """ testing access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        """ testing access_nested_map error handling"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """testing get_json class """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
    ) -> None:
        """testing get_json"""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ testing Memoize """
    def test_memoize(self) -> None:
        """test_memoize doc"""

        class TestClass:
            """TestClass doc"""

            def a_method(self) -> int:
                """a_method doc"""
                return 42

            @memoize
            def a_property(self) -> int:
                """ a_property doc"""
                return self.a_method()
        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mocked.assert_called_once()
