# content of test_assert3_matching_exception_message.py

import pytest

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match = r".* 123 .*"):
        myfunc()

# pytest test_assert3_matching_exception_message.py