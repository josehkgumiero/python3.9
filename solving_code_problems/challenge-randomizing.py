import random

# help(random.random)

print(
    random.random()
)

_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

print(
    sorted(
        _list,
        key = lambda x: random.random()
    )
)