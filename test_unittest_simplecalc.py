# Let's create tests to check if the code would be running without any errors

# Importing the file and class where we would write our code
from simple_calc import SimpleCalc

# Importing unittest to inherit TestCase to create our tests against the code
import unittest

class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):  # naming convention - using `test` in the name of the function will let python interpreter know that this needs to be tested
        # 2 + 2 = 4 outcome is True
