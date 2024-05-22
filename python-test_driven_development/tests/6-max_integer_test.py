#!/usr/bin/python3
"""
UNITTEST module for testing max_integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class for unit tests of the max_integer function.
    """
    
    def test_max_integer(self):
        """
        Test different possible cases for the max_integer function,
        including edge cases.
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([15, 10, 5]), 15)
        self.assertEqual(max_integer([15, 10, 5, -5, -10, 15]), 15)
        self.assertEqual(max_integer([15, 15, 15]), 15)
        self.assertEqual(max_integer([15, 20, 15]), 20)
