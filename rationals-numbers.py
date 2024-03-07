from fractions \
import Fraction

# help(Fraction)


print(
    Fraction(1)
)

print(
    Fraction(
        denominator = 1,
        numerator = 2
    )
)

print(
    Fraction(
        numerator = 1,
        denominator = 2
    )
)

print(
    Fraction(
        0.125
    )
)

print(
    Fraction(
        '''0.125'''
    )
)

print(
    Fraction(
        '''22/7'''
    )
)

a = Fraction(2, 3)

b = Fraction(3, 4)

print(
    a + b
)

print(
    a * b
)

print(
    a / b
)

print(
    Fraction(8 , 16)
)

print(
    Fraction(1, -4)
)

c = Fraction(1, -4)

print(
    c.numerator
)

print(
    c.denominator
)

import math

d = Fraction(math.pi)

print(
    d
)

print(
    float(
        d
    )
)

e = Fraction(
    math.sqrt(
        2
    )
)

print(
    e
)

print(
    float(
        e
    )
)

f = 0.3

print(
    format(
        f,
        '0.5f'
    )
)

print(
    format(
        f,
        '0.15f'
    )
)

print(
    format(
        f,
        '0.25f'
    )
)

print(
    Fraction(f)
)

g = Fraction(0.3)

g.limit_denominator(10)

g = Fraction(
    math.pi
)

print(
    g
)

print(
    float(
        g
    )
)

print(
    g \
        .limit_denominator(10)
)

print(
    g \
        .limit_denominator(100000)
)