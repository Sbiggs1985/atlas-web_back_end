#!/usr/bin/env python3
"""Unittests for utils module

This module contains unittests for the utility functions
Defined in the utils module.
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestClass:
    """Class to be tested"""

    def a_method(self):
        # Defining the a_method
        return 42

    @memoize
    # @memoize patch
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """TestMemoize class that inherits from unittest.TestCase"""

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method):
        """Test that memoization works as expected"""

        # Create an instance of TestClass
        test_instance = TestClass()

        # Call a_property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Assert that the method was called only once and results are correct
        mock_method.assert_called_once()
        self.assertEqual(result1, result2)
        self.assertEqual(result1, 42)


if __name__ == "__main__":
    # the name = main
    unittest.main()
