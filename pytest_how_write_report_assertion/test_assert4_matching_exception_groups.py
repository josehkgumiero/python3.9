# content of test_assert4_matching_exception_groups.py

import pytest

def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError("Exception 123 raised"),
            ],
        )
    assert excinfo.group_contains(RuntimeError, match=r".* 123 .*")
    assert not excinfo.group_contains(TypeError)

def test_exception_in_group_at_given_depth():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
                ExceptionGroup(
                    "Nested group",
                    [
                        TypeError(),
                    ],
                ),
            ],
        )
    assert excinfo.group_contains(RuntimeError, depth=1)
    assert excinfo.group_contains(TypeError, depth=2)
    assert not excinfo.group_contains(RuntimeError, depth=2)
    assert not excinfo.group_contains(TypeError, depth=1)

# pytest test_assert4_matching_exception_groups.py