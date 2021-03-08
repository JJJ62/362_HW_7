import unittest
from FizzBuzz import is_Fizz
from FizzBuzz import is_Buzz
from FizzBuzz import print_num
from FizzBuzz import main
# Read program specification
# Write initial test and run it to ensure it fails
# Commit changes, Example: "Wrote first test, {test description}”
# Write code just enough to pass the test
# Run a test to verify if it passed
# Commitchanges,"Implemented x method{implementationdescription}"
# Write second test

num_array = list(range(1, 101))
class TestFizzBuzz(unittest.TestCase):
    def test_Fizz(self):
        result = is_Fizz(3)
        self.assertEqual(result, 1)
        result = is_Fizz(15)
        self.assertEqual(result, 1)
        result = is_Fizz(2)
        self.assertEqual(result, 0)
    def test_Buzz(self):
        result = is_Buzz(5)
        self.assertEqual(result, 1)
        result = is_Buzz(10)
        self.assertEqual(result, 1)
        result = is_Buzz(2)
        self.assertEqual(result, 0)
    def test_num(self):
        result = print_num()
        self.assertEqual(result, num_array)
    #if the nuber of Fizz and FizzBuzz are correct it returns 1
    def test_whole():
        result = main()
        self.assertEqual(result, 1)
