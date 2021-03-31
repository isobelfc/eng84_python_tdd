# TDD - Test Driven Development
## Why should we use TDD
### What are the benefits of using TDD

**Best use cases**
- We will use Pytest unittest in Python to implement TDD
- TDD is widely used and is the cheapest way to test the code or implement test driven development

**Best practices for TDD**
- Write the smallest possible test case that matches what we need to program
- TDD cycle starts with everything failing - `RED`
- Write code to pass the test `GREEN`
- Refactor the code for the next test `BLUE`
- This goes on until all the tests have successfully passed
  
![TDD Cycle](https://gorillalogic.com/wp-content/uploads/2016/08/70087690-1.png)
- Assertions are important in testing

|Method |   Checks that|   New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |    a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b             |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b         |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2|

- Let's create a file called `test_unittest_simplecalc.py`
- Naming convention is extremely important when it comes to TDD in Python
- It enables the testing software to find the right file and run it correctly
- We need separate files for testing and code
```python
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
```
- Run the tests `python -m pytest`

**Let's write our code now to pass the tests**
```python
class SimpleCalc():
    # pass
    def add(self, value1, value2):
        return value1 + value2
        # this function adds the values for value1 and value2 against the test we have in other class

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

# run this file after defining each function to check there are no syntax errors
```

- Running the tests with `python -m unittest discover -v`
```
python -m unittest discover -v
test_add (test_unittest_simplecalc.CalcTest) ... ok
test_divide (test_unittest_simplecalc.CalcTest) ... ok
test_multiply (test_unittest_simplecalc.CalcTest) ... ok
test_subtract (test_unittest_simplecalc.CalcTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```