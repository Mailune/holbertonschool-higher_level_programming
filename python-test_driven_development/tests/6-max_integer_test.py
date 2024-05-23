#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test with an unsorted list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_numbers(self):
        """Test with a list containing float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_single_element_list(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_mixed_list(self):
        """Test with a mixed list of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()
