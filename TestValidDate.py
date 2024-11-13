"""
OPS435 Assignment 1 - Summer 2023
File: TestValidDate.py
Author: Tandin Wangmo

This script contains unit tests for the valid_date() function in assignment1.py.
It verifies that valid_date() correctly validates dates, checking for valid format,
range, and leap year considerations.
"""

import unittest
from assignment1 import valid_date

class TestValidDateFunction(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(valid_date("2023-02-28"))  # Standard valid date
        self.assertTrue(valid_date("2024-02-29"))  # Valid leap day
        self.assertTrue(valid_date("2000-02-29"))  # Valid leap day in a century year

    def test_invalid_date(self):
        self.assertFalse(valid_date("2023-02-30"))  # Invalid date
        self.assertFalse(valid_date("1900-02-29"))  # Not a leap year
        self.assertFalse(valid_date("2023-04-31"))  # April has only 30 days
        self.assertFalse(valid_date("abcd-ef-gh"))  # Invalid format

if __name__ == '__main__':
    unittest.main()
