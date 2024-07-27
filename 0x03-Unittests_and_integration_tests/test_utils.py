#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
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


if __name__ == "__main__":
    unittest.main()