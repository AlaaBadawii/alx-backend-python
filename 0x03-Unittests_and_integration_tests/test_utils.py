#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize
from unittest.mock import Mock, patch
from utils import get_json

"""
test_utils module
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1,),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test_access_nested_map fun
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        test_access_nested_map_exception fun
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """test_get_json fun"""
        with unittest.mock.patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""
    def test_memoize(self):
        """test_memoize method"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_m:
            instance = TestClass()
            # Call a_property twice
            result1 = instance.a_property
            result2 = instance.a_property

            # Check the return value
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method is called only once
            mock_m.assert_called_once()


if __name__ == "__main__":
    unittest.main()
