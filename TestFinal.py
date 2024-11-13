"""
OPS435 Assignment 1 - Summer 2023
File: TestFinal.py
Author: Tandin Wangmo

This script runs integration tests for assignment1.py to verify that the main program
correctly handles command-line arguments, calculates weekend days, and displays output
for various scenarios, including error handling and reversed dates.
"""


import unittest
import subprocess

class TestFinalScript(unittest.TestCase):
    def test_final_output(self):
        # Test for a full month with the correct expectation of 9 weekend days
        result = subprocess.run(
            ["python3", "assignment1.py", "2023-01-01", "2023-01-31"],
            capture_output=True, text=True
        )
        self.assertIn("9 weekend days", result.stdout)

    def test_final_output_reversed_dates(self):
        # Test with reversed date input order, expecting 9 weekend days
        result = subprocess.run(
            ["python3", "assignment1.py", "2023-01-31", "2023-01-01"],
            capture_output=True, text=True
        )
        self.assertIn("9 weekend days", result.stdout)

    def test_final_invalid_date(self):
        # Test with an invalid date to check for the usage message
        result = subprocess.run(
            ["python3", "assignment1.py", "2023-02-30", "2023-03-01"],
            capture_output=True, text=True
        )
        self.assertIn("Usage", result.stdout)  # Expect a 
