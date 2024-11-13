"""
OPS435 Assignment 1 - Summer 2023
File: TestMonMax.py
Author: Tandin Wangmo

This script contains unit tests for the mon_max() function in assignment1.py.
It checks that mon_max() returns the correct maximum number of days for each month,
including adjustments for leap years.
"""


import unittest
from assignment1 import mon_max

class TestMonMaxFunction(unittest.TestCase):
    def test_january(self):
        self.assertEqual(mon_max(1, 2023), 31)  # January has 31 days

    def test_february_non_leap(self):
        self.assertEqual(mon_max(2, 2023), 28)  # February (non-leap year) has 28 days

    def test_february_leap(self):
        self.assertEqual(mon_max(2, 2024), 29)  # February (leap year) has 29 days

    def test_april(self):
        self.assertEqual(mon_max(4, 2023), 30)  # April has 30 days

if __name__ == '__main__':
    unittest.main()
