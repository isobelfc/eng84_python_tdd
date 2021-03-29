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