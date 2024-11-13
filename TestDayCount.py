"""
OPS435 Assignment 1 - Summer 2023
File: TestDayCount.py
Author: Tandin Wangmo

This script contains unit tests for the day_count() function in assignment1.py.
It tests that day_count() accurately calculates the number of weekend days between
two given dates.
"""


import unittest
from assignment1 import day_count

class TestDayCountFunction(unittest.TestCase):
    def test_day_count_standard(self):
        self.assertEqual(day_count("2023-01-01", "2023-01-31"), 9)  # Corrected to 9 weekend days

    def test_day_count_single_weekend(self):
        self.assertEqual(day_count("2023-01-07", "2023-01-08"), 2)  # One weekend (Saturday and Sunday)
        self.assertEqual(day_count("2023-01-06", "2023-01-07"), 1)  # Friday to Saturday has 1 weekend day

    def test_day_count_with_leap_year(self):
        self.assertEqual(day_count("2024-02-01", "2024-02-29"), 8)  # February 2024 has 8 weekend days

if __name__ == '__main__':
    unittest.main()
