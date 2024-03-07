l = [
    1,
    2,
    3,
    4,
    5,
    6
]

a = l[0]

b = l[1:]

print(
    a
)

print(
    b
)

c, d = l[0], l[1:]

print(
    c
)

print(
    d
)

e, *f = l

print(
    e
)

print(
    f
)

j = 'python'

m = ('a', 'b', 'c')

a, *b = m

print(
    a,
    b
)

[a, b, c] = 'XYZ'

print(
    a,
    b,
    c
)

a, b, *c = 'python'

print(
    a,
    b,
    c
)

a, b, *c, d = 'python'

print(
    a,
    b,
    c,
    d
)

_python = 'python'

a, b, c, d = _python[0], _python[1], _python[2:-1], _python[-1]

print(
    a,
    b,
    c,
    d
)

l1 = [1, 2, 3]

l2 = [4, 5, 6]

l3 = [*l1, *l2]

print(
    l
)

l1 = [1, 2, 3]

_s = 'abc'

print(
    [*l1, *_s]
)

_s1 = {'x', 'y', 'z'}

print(
    [*l1, *_s]
)

_s2 = 'abc'

_s3 = 'cde'

print(
    [*_s2, *_s3]
)

print(
    {*_s2, *_s3}
)

xyz = {10, -99, 3, 'd'}

for c in xyz:
    print(c)

a, b, c, d = xyz

print(
    a,
    b,
    c,
    d
)

a, b, *c = xyz

print(
    a,
    b,
    c
)

print(
    list(
        xyz
    )
)

_dict1 = {1, 2, 3}

_dict2 = {4, 5, 6}

_dict3 = {8, 9, 10}

_dict4 = {11, 12, 13}

_dict3 = {*_dict1, *_dict2}

print(
    _dict3
)

# help(set)

print(
    _dict1.union(_dict2)
)

print(
    _dict1.union(_dict2).union(_dict3).union(_dict4)
)

print(
    _dict1.union(_dict2, _dict3, _dict4)
)

print(
    [
        *_dict1,
        *_dict2,
        *_dict3,
        *_dict4
    ]
)

print(
    {
        *_dict1,
        *_dict2,
        *_dict3,
        *_dict4
    }
)

_d1 = {
    'key1': 1,
    'key2': 2
}

_d2 = {
    'key3': 3,
    'key4': 4
}

print(
    {
        *_d1,
        *_d2
    }
)

print(
    {
        **_d1,
        **_d2
    }
)

print(
    {
        **_d2,
        **_d1
    }
)

print(
    {
        'a': 1,
        'b': 2,
        **_d1,
        'c':3
    }
)

a, b, e = [1, 2, 'XY']

print(
    a,
    b,
    e
)

c, d = e

print(
    c,
    d
)

a, b, (c, d) = [1, 2, 'XY']

print(
    a,
    b, 
    c,
    d
)

a, b, (c, d, *e) = [1, 2, 'python']

l = [1, 2, 3, 4, 'python']

a, *b, (c, d, *e) = l

print(
    a,
    b,
    c,
    d,
    e
)

print(
    l[0],
    l[1:-1],
    l[-1][0],
    l[-1][1],
    list(l[-1][2:])
)

