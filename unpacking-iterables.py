a = (1, 2, 3)

print(
    type(
        a
    )
)

b = 1, 2, 3

print(
    type(
        b
    )
)

print(
    b
)

c = (1)

d = ('a')

e = (1, )

print(
    c,
    d,
    e
)

f = 100,

print(
    f,
    type(
        f
    )
)

g = ()

print(
    type(
        g
    )
)

h, i, j = [1, 'a', 3.14]

print(
    h,
    i,
    j
)

(k, l, m) = [1, 2, 3]

print(
    k,
    l,
    m
)

n, o = 10, 20

print(
    n,
    o
)

p, q, r = 10, 20, 30

print(
    p,
    q,
    r
)

s, t, u = 10, {1, 2}, ['a', 'b']

print(
    s,
    t,
    u
)

for e in 'XYZ':
    print(e)

a, b, c = 'XYZ'

print(
    a,
    b,
    c
)

v = {1, 2, 3}

x = {'p', 'y', 't', 'h', 'o', 'n'}

for _x in x:
    print(_x)

a, b, c, d, e, f = x

print(
    a,
    b,
    c,
    d,
    e,
    f
)

y = {
    'a': 1,
    'b': 2,
    'c': 3
}

for _y in y:
    print(_y)

w = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

a, b, c, d = w

print(
    a,
    b,
    c,
    d
)

_python_string = {
    'a': 'p', 
    'b': 'y', 
    'c': 't', 
    'd': 'h', 
    'e': 'o', 
    'f': 'n'
}

for _letters in _python_string:
    print(_letters)

for _letters in _python_string.values():
    print(_letters)

_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

for _a, _b in _dict.items():
    print(
        '''key = {0}, value = {1}''' \
        .format(_a, _b)
    )