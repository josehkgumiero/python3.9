# help(sorted)

_random_list = [1, 5, 4, 10, 9, 6] 

print(
    sorted(_random_list)
)

_random_letters_list = ['c', 'B', 'D', 'a']

print(
    sorted(
        _random_letters_list
    )
)

print(
    ord(
        'a'
    )
)

print(
    ord(
        'A'
    )
)

print(
    sorted(
        _random_letters_list,
        key = lambda s: s.upper()
    )
)

a = {
    'def': 300,
    'abc': 200,
    'ghi': 100
}

for e in a:
    print(e)

print(
    sorted(
        a
    )
)

print(
    sorted(
        a,
        key = lambda e: a[e]
    )
)

def dist_eq(x):
    return (x.real)**2 + (x.imag)**2

print(
    dist_eq(1 + 1j)
)

_list_complex = [3 + 3j, 1 - 1j, 0, 3 + 0j]

print(
    sorted(
        _list_complex,
        key = dist_eq
    )
)

print(
    _list_complex,
    key = lambda x: (x.real)**2 + (x.imag)**2
)

_list_name = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(
    _list_name
)

print(
    sorted(_list_name)
)

print(
    sorted(
        _list_name,
        key = lambda s: s[-1]
    )
)
