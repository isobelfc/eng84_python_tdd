# Let's create tests to check if the code would be running without any errors

# Importing the file and class where we would write our code
from simple_calc import SimpleCalc

# Importing unittest to inherit TestCase to create our tests against the code
import unittest

class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):  # naming convention - using `test` in the name of the function will let python interpreter know that this needs to be tested
        self.assertEqual(self.calc.add(2, 4), 6)
        # this test is checking if 2 + 4 = 6, if true test will pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        # this tests the values as 4 - 2 = 2, if true test will pass

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        # this tests the values 2 * 2 = 4, if true the test passes

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)
        # this tests 15 / 3 = 5, if true the test passes

# `python -m pytest` in the terminal runs the tests
# run it before starting, and then again after defining each method
# pytest looks for any file with name including test*.py
