print(
    'a' \
    or [1, 2]
)

print(
    '' \
    or [1, 2]
)

print(
    1 or 1/0
)

s1 = None
s2 = ''
s3 = 'abc'

s1 = s1 or 'n/a'
s2 = s1 or 'n/a'
s3 = s3 or 'n/a'

print(
    s1,
    s2,
    s3
)

print(
    [] or [0]
)

print(
    None or [0]
)

print(
    None and 100
)

print(
    [] and [0]
)

a = 2

b = 0


try:
    print(
        a / b
    )
except Exception:
    print(Exception)

c = 2

d = 4

if b == 0:
    print(0)
else:
    print(a / b)

e = 2

f = 0

try:
    print(
        e and e / f
    )
except Exception:
    print(Exception)

g = 2

h = 0

try:
    print(g and g / h)
except Exception:
    print(Exception)

s4 = None

s5 = ''

s6 = 'abc'

print(
    s6[0]
)

print(
    (
        (s4 and s4[0]) or 'n/a'
    )
)

print(
    (
        (s5 and s5[0]) or 'n/a'
    )
)

print(
    (
        (s6 and s6[0]) or 'n/a'
    )
)

# help(bool)

print(
    0.1 is (3 + 4j)
)

print(
    3 is 3
)

print(
    [1, 2] is [1, 2]
)

print(
    'a' in 'this is a test'
)

print(
    3 in [1, 2, 3]
)

print(
    3 not in [1, 2, 3]
)

print(
    'key1' in {'key1': 1}
)

print(
    1 in {'key1': 1}
)

print(
    3 < 5
)

try:
    print(
        1 + 1j < 3 + 4j
    )
except Exception:
    print(Exception)

from decimal import Decimal
from fractions import Fraction

print(
    4 < Decimal('10.5')
)

print(
    Fraction(2, 3) < Decimal('0.5')
)

try:
    print(
        4 == 4 + 0j
    )
except Exception:
    print(Exception)

print(
    True == Fraction(2, 2)
)

print(
    True < Fraction(3, 2)
)

print(
    1 < 2 < 3
)

print(
    1 < 2 and 2 < 3
)

print(
    3 < 2 < 1 / 0
)

print(
    3 < 2 and 2 < 1 / 0
)

try:
    print(
        3 < 4 < 1 / 0
    )
except Exception:
    print(Exception)

print(
    1 < 2 > -5
)

print(

    1 < 2 > -5 == Decimal('-5.0')
)

import string

print(
    'A' < \
    'a' < \
    'z' > \
    'Z' in string.ascii_letters
)