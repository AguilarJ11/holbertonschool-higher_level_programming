#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def cool_o(self):
        self.assertEqual(max_integer([1, 2]), 2)
    def cool_os(self):
        self.assertEqual(max_integer([]), None)
    