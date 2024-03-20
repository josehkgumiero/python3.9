# help(complex)

a = complex(1, 2)

b = 1 + 2j

print(
    a == b
)

print(
    a.real,
    type(
        a.real
    )
)

print(
    a.imag,
    type(
        a.imag
    )
)

print(
    a \
    .conjugate()
)

c = 1 + 2j

d = 10 + 8j

print(
    c + d
)

print(
    c * d
)

print(
    a / b
)

print(
    a ** 2
)

try:
    print(
        a // 2
    )
except Exception as error:
    print(error)

try:
    print(
        a % 2
    )
except Exception as error:
    print(error)

try:
    print(
        divmod(a, b)
    )
except Exception as error:
    print(error)

c = 0.1j

print(
    format(
        c.imag,
        '.25f'
    )
)

import math

print(
    math \
    .sqrt(2)
)