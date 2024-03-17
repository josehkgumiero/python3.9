# content of test_assert2_expected_exceptions.py

import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)

def test_foo_not_implemented():
    def foo():
        raise NotImplementedError

    with pytest.raises(RuntimeError) as excinfo:
        foo()
    assert excinfo.type is RuntimeError

# pytest test_assert2_expected_exceptions.py