"""
OPS435 Assignment 1 - Summer 2023
File: TestAfter.py
Author: Tandin Wangmo

This script contains unit tests for the after() function in assignment1.py.
It checks that after() correctly returns the next day’s date for given input dates,
including handling month and year transitions.
"""

import unittest
from assignment1 import after

class TestAfterFunction(unittest.TestCase):
    def test_after_standard_date(self):
        self.assertEqual(after('2023-01-25'), '2023-01-26')  # Standard next day

    def test_after_month_end(self):
        self.assertEqual(after('2023-01-31'), '2023-02-01')  # Month-end transition

    def test_after_year_end(self):
        self.assertEqual(after('2023-12-31'), '2024-01-01')  # Year-end transition

    def test_after_february_non_leap(self):
        self.assertEqual(after('2023-02-28'), '2023-03-01')  # End of February (non-leap year)

    def test_after_february_leap(self):
        self.assertEqual(after('2024-02-28'), '2024-02-29')  # February leap year transition

if __name__ == '__main__':
    unittest.main()
