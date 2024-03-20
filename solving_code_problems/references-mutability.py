a = '''hello'''
b = 0
c = '''hello'''

print(
    hex(
        id(
            a
        )
    )
)

print(
    hex(
        id(
            b
        )
    )
)

print(
    hex(
        id(
            c
        )
    )
)

d = [
    1,
    2,
    3
]

e = d

print(
    hex(
        id(
            e
        )
    )
)

print(
    hex(
        id(
            d
        )
    )
)

d.append(4)

print(
    hex(
        id(
            e
        )
    )
)

print(
    hex(
        id(
            d
        )
    )
)