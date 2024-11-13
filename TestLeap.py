"""
OPS435 Assignment 1 - Summer 2023
File: TestLeap.py
Author: Tandin Wangmo

This script contains unit tests for the leap_year() function in assignment1.py.
It verifies that leap_year() accurately identifies leap years, including cases for
century and non-century years.
"""


import unittest
from assignment1 import leap_year

class TestLeapYearFunction(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(leap_year(2024))    # 2024 is a leap year
        self.assertFalse(leap_year(1900))   # 1900 is not a leap year
        self.assertTrue(leap_year(2000))    # 2000 is a leap year
        self.assertFalse(leap_year(2023))   # 2023 is not a leap year

if __name__ == '__main__':
    unittest.main()
