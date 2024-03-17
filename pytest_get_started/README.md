# Pytest Get Started
# Create Virtual Environment
```
mkdir pytest_get_started
cd pytest_get_started
python3 -m venv .venv
```
# Start Virtual Environment
```
source .venv/bin/activate
```
# Install Pytest
```
pip install -U pytest
```
# Check the Version of Pytest
```
pytest --version
```
# Create a new file
```
touch test_sample.py
```
# Create your first test
- Create a new file called test_sample.py, containing a function, and a test:
```
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```
```
pytest
```
# Run multiple tests
- pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.
```
touch test_sample_raise_sysexit.py
```
```
# content of test_sample_raise_sysexit.py
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
```
```
pytest -q test_sample_raise_sysexit.py
```
```
touch test_sample_raise_exceptiongroup.py
```
```
# content of test_sample_raise_exceptiongroup.py
import pytest

def f():
    raise ExceptionGroup(
        "Group message",
        [
            RuntimeError(),
        ],
    )

def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        f()
    assert excinfo.group_contains(RuntimeError)
    assert not excinfo.group_contains(TypeError)
```
```
pytest -q test_sample_raise_exceptiongroup.py
```
```
touch test_class.py
```
```
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x
    
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
```
```
pytest -q test_class.py
```
```
touch test_class_demo.py
```
```
# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
```
```
pytest -k TestClassDemoInstance -q
```
```
touch test_tmp_path.py
```
```
# content of test_tmp_path.py
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0
```
```
pytest -q test_tmp_path.py
```