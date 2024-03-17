# content of test_assert5_alternate_form.py

import pytest

def func(x):
    if x <= 0:
        raise ValueError("x needs to be larger than zero")


def test():
    pytest.raises(ValueError, func, x=-1)

# pytest test_assert5_alternate_form.py