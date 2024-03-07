def process(s):
    print(
        '''Initial s # = {0}''' \
        .format(id(s))
    )
    s = s + '''world'''
    print(
        '''Final s # = {0}'''\
        .format(id(s))
    )

a = '''Hello'''

print(
    '''a # = {0}''' \
    .format(id(a))
)

process(a)

print(
    id(
        a
    )
)

print(
    a
)

def modify_list(b):
    print(
        '''Initial lst # = {0}''' \
        .format(
            id(
                b
            )
        )
    )
    b.append(100)
    print(
        '''FInal lst # = {0}''' \
        .format(
            id(
                b
            )
        )
    )

c = [
    1,
    2,
    3
]

print(
    id(
        c
    )
)

modify_list(
    c
)

def modify_tuple(d):
    print(
        '''Initial t # = ''' \
        .format(
            id(
                d
            )
        )
    )
    d[0].append(100)
    print(
        '''FInal t # = {0}''' \
        .format(
            id(
                d
            )
        )
    )

e = ([1, 2], 'a')

print(
    id(
        e
    )
)

modify_tuple(e)