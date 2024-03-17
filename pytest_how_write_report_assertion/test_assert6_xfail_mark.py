# content of test_assert6_xfail_mark.py

import pytest

def f():
    raise IndexError()


@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()

# pytest test_assert6_xfail_mark.py