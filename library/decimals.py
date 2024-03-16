import decimal

print(
    decimal \
        .getcontext()
)

print(
    decimal \
        .getcontext() \
        .rounding
)

print(
    decimal \
        .getcontext() \
        .prec
)

decimal \
    .getcontext() \
    .prec \
    = 6

print(
    decimal \
    .getcontext() \
    .prec
)

g_ctx = decimal \
    .getcontext()

print(
    type(
        g_ctx
    )
)

g_ctx \
    .rounding \
    = 'ROUND_HALF_UP'

print(
    g_ctx \
    .rounding
)

print(
    type(
        decimal \
        .localcontext()
    )
)

from decimal \
import Decimal

x = Decimal('1.25')

y = Decimal('1.35')

with decimal.localcontext() \
    as ctx:
        ctx \
        .prec \
        = 6
        ctx \
        .rounding \
        = decimal \
        .ROUND_HALF_UP
        print(
                round(x, 1)
        )
        print(
                round(y, 1)
        )
print(
        round(x, 1)
)
print(
        round(y, 1)
)
