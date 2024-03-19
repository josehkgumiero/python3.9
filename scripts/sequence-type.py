# Sequence type
l = [
        1,
        2,
        3
    ]

t = (
        1,
        2,
        3
    )

p = 'python'

print(
    l
)

print(
    t
)

print(
    p
)

print(l[0])

print(t[1])

print(p[2])

for c in p:
    print(c)

s = {10, 20, 30}

for e in s:
    print(e)

a = {'x', 10, 'a', 'A'}

for _a in a:
    print(_a)

try:
    t[0] = 100
except Exception as e:
    print(e)

t = ([1, 2], 3, 4)

try:
    t[0] = [1, 2, 3]
except Exception as e:
    print(e)

print(t)

print(t[0])

t[0][0] = 100

print(t)

print('a' in ['a', 'b', 100])

print(100 in range(200))

print(len('python'), len([1, 2, 3]), len({10, 20, 30}),len({'a': 1, 'b': 2}))

print(100 < 2000)

l = [100, 90, 20]

print(l)

print(min(l))

print(max(l))

l = ['a', 'b', 'c']

print('a' < 'b')

from decimal import Decimal

l = [10, 10.5, Decimal('20.3')]

print(l)

print(min(l))

print([1, 2, 3] + [4, 5, 6])

print((1, 2, 3) + (4, 5, 6))

try:
    print('abc' + ['d', 'e', 'f'])
except Exception as e:
    print(e)

print(list('abc'))

print(list('abc') + ['d','e','f'])

print(','.join(['1', '2', '3']))

print(','.join(list('abc') + ['d', 'e', 'f']))

print('abc' * 3)

print([1, 2, 3] * 3)

s = "gnu's not unix"

print(list(enumerate(s)))

s = 'python'

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(s[1:4])

print(list(enumerate(s)))

print(l[0:5])

print(s[4:1000])

l = [1, 2, 3]

l2 = l[:]

print(l, l2)

print(id(l), id(l2), l is l2)

a = Decimal('10.5')

b = Decimal('10.5')

print(a is b)

print(id(a), id(b))

print(a == b)