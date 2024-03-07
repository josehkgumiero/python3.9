print(
    type(
        1 + 1
    )
)

print(
    type(
        2 * 3
    )
)

print(
    type(
        4 - 10
    )
)

print(
    type(
        3 ** 6
    )
)

print(
    type(
        2 / 3
    )
)

print(
    type(
        10 / 2
    )
)

import math

print(
    math.floor(
        3.15
    )
)

print(
    math.floor(
        3.9999999
    )
)

print(
    math.floor(
        -3.14
    )
)

print(
    math.floor(
        -3.0000001
    )
)

a = 33

b = 16

print(
    a / b
)

print(
    a // b
)

print(
    math.floor(
        a / b
    )
)

c = -33

d = 16

print(
    a / b
)

print(
    a // b
)

print(
    math.floor(
        a / b
    )
)

e = 13

f = 4

print(
    '''{0}/{1} = {2}''' \
    .format(a, b, a / b)
)

print(
    '''{0}//{1} = {2}''' \
    .format(a, b, a // b)
)

print(
    '''{0}%{1} = {2}''' \
    .format(a, b, a % b)
)

print(
    a == b * ( a // b ) + ( a % b )
)