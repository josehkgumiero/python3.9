from decimal \
import Decimal

print(
    Decimal(10)
)

print(
    Decimal(-10)
)

print(
    Decimal('10.1')
)

print(
    Decimal('-3.1415')
)

t = \
    (0, (3, 1, 4, 5), -4)

print(
    Decimal(
        (1, (3, 1, 4, 1, 5), -3)
    )
)

print(
    format(
        0.1,
        '.25f'
    )
)

print(
    Decimal(0.1)
)

print(
    Decimal('0.1')
)

print(
    Decimal(0.1) == Decimal('0.1')
)

print(
    Decimal(10) == Decimal('10')
)

a = Decimal('0.12345')

b = Decimal('0.12345')

print(
    a + b
)

import decimal

with decimal \
    .localcontext() \
        as ctx:
    ctx.prec = 2
    c = a + b
    print(
        '''c withiin local context: {0}''' \
        .format(c)
    )
print(
    '''c within local context: {0}''' \
    .format(c)
)
