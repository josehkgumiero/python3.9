a = [
    1,
    2,
    3
]

print(
    type(
        a
    )
)

print(
    id(
        a
    )
)

a.append(4)

print(
    a
)

print(
    id(
        a
    )
)

b = dict(key1 = 1, key2 = 'c')

print(
    b
)

print(
    id(
        b
    )
)

b['''key3'''] = 10.5

print(
    b
)

print(
    id(
        b
    )
)

t = (1, 2, 3)

print(
    id(
        t
    )
)

t = ([1, 2], [3, 4])

print(
    id(
        t
    )
)