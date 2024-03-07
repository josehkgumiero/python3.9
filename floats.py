from fractions \
import Fraction

# help(float)

print(
    float(
        10
    )
)

print(
    float(
        10.4
    )
)

print(
    float(
        '12.5'
    )
)

print(
    float(
        Fraction(
            '22/7'
        )
    )
)

a = Fraction(22, 7)

print(
    float(a)
)

print(
    0.1
)

print(
    format(
        0.1,
        '.15f'
    )
)

print(
    format(
        0.1,
        '.25f'
    )
)

print(
    0.125
)

print(
    format(
        0.125,
        '.25f'
    )
)

a = 0.1 + 0.1 + 0.1

b = 0.3

print(
    a == b
)

print(
    format(
        a,
        '.25f'
    )
)

print(
    format(
        b,
        '.25f'
    )
)