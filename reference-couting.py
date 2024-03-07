a = [
    1,
    2,
    3
]

a_id = id(a)

import sys

print(
    sys.getrefcount(
        a
    )
)

import ctypes

def ref_count(address: int):
    return \
        ctypes.c_long.from_address(address).value

print(
    ref_count(
        id(
            a
        )
    )
)

print(
    ref_count(
        a_id
    )
)

b = a

c = a

print(
    ref_count(
        id(
            b
        )
    )
)

print(
    ref_count(
        id(
            c
        )
    )
)

print(
    id(
        b
    )
)

b = None

print(
    id(
        b
    )
)