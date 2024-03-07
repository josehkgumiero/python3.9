a = 0.1

print(
    format(
        a,
        '.25f'
    )
)

print(
    a
)

b = 0.125

print(
    format(
        b,
        '.25f'
    )
)

c = 0.125 + 0.125 + 0.125

d = 0.375

print(
    c == d
)

print(
    format(
        c,
        '.25f'
    )
)

print(
    format(
        d,
        '.25f'
    )
)

print(
    round(c, 3) == round(d, 3)
)

e = 10000.01

f = 10000.02

print(
    e / f
)

g = 0.01

h = 0.02

print(
    g / h
)

print(
    round(g, 1) == round(h, 1)
)

from math \
import isclose

# help(isclose)

i = 123456789.01

j = 123456789.02

isclose(
    i,
    j,
    rel_tol = 0.01
)

k = 0.01

l = 0.02

isclose(
    k,
    l,
    rel_tol = 0.01
)

