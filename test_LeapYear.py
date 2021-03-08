import unittest
from LeapYear import is_leapyear

# Read program specification
# Write initial test and run it to ensure it fails
# Commit changes, Example: "Wrote first test, {test description}”
# Write code just enough to pass the test
# Run a test to verify if it passed
# Commitchanges,"Implemented x method{implementationdescription}"
# Write second test

class TestLeap(unittest.TestCase):
    def test_leap(self):
        result = is_leapyear(2000)
        self.assertEqual(result, 1)
        result = is_leapyear(2024)
        self.assertEqual(result, 1)
        result = is_leapyear(2001)
        self.assertEqual(result, 0)
