#!/usr/bin/python3
"""
Unittests for the function def max_integer(list=[])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """Define unititests for max_integer."""

    def test_empty_list(self):
        """Test an empty list."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """Test a single element."""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """Test positive numbers."""
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test negative numbers."""
        result = max_integer([-5, -4, -3, -2, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test negative and positive numbers."""
        result = max_integer([-3, 0, 10, -5, 6])
        self.assertEqual(result, 10)

    def test_duplicate_values(self):
        """Test duplicate values."""
        result = max_integer([1, 2, 3, 3, 2, 1])
        self.assertEqual(result, 3)

    def test_empty_list_with_default_parameter(self):
        """Test an empty list with defal parameter."""
        result = max_integer()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
