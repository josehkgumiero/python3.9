def add_item(
        name,
        quantity,
        unit,
        grocery_list = []
):
    grocery_list.append(
        '''
        {0} ({1} {2})
        ''' \
        .format(
            name,
            quantity,
            unit
        )
    )
    return grocery_list

store1 = []

store2 = []

add_item(
    '''banana''',
    2,
    '''units''',
    store1
)

add_item(
    '''milk''',
    1,
    '''liter''',
    store1
)

print(
    store1
)

add_item(
    'python',
    1,
    '''medium-rare''',
    store2
)

print(store2)

del store1

del store2

store1 = add_item('banana', 2, 'units')

add_item('milk', 1, 'liter', store1)

print(store1)

store2 = add_item('python', 1, 'medium-rare')

print(store2)

def add_item(name, quantity, unit = 1, grocery_list = None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append(
        '''
        {0} ({1} {2})
        ''' \
        .format(name, quantity, unit)
    )
    return grocery_list

store1 = add_item('banana', 2, 'units')

add_item('milk', 1, 'liter', store1)

print(store1)

store2 = add_item('python', 1, 'medium-rare')

print(store2)

print(
    store1 is store2
)

def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n - 1)

factorial(3)

def factorial(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n - 1, cache = cache)
        cache[n] = result
        return result

cache = {}

factorial(3, cache = cache)

