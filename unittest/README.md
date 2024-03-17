# Unit testing framework

# unittest

- It was inspired by JUnit;
- It supports:
    - test automation
    - sharing of setup
    - shutdown code for tests
    - aggregation of tests into collections
    - independence of the tests from the reporting framework
- It supports concepts in an object-oriented way:
    - test fixture
    - test case
    - test suite
    - test runner

- Here is a short script oto lest three string methods:
```
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

- The unittestmodule can be used from the command line to run tests from modules, classes or even individual test methods:
```
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
python -m unittest tests/test_something.py
```

- For a ist of all the command line options:
```
python -m unittest -h
```

- Test discovery:
```
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"
```