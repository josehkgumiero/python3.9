from random import randint, random

from collections import namedtuple

Color = namedtuple('Color', 'red green bue alpha')

def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)

color = random_color()

red, green, blue, alpha = color

print(red, alpha)

print(color)

print(color.red)

print(color.alpha)

print(Color._fields)

data_dict = dict(key1 = 100, key2 = 200, key3 = 300)

print(data_dict['key1'])

from collections import namedtuple

print(data_dict.keys())

Data = namedtuple('Data', data_dict.keys())

print(Data._fields)

print(data_dict.values())

d1 = Data(*data_dict.values())

print(d1)

d2 = Data(key1 = 10, key2 = 20, key3 = 30)

print(d2)

Data = namedtuple("Data", "key3 key2 key1")

print(Data._fields)

d3 = Data(*data_dict.values())

print(d3)

d4 = Data(**data_dict)

print(d4)

key_name = 'key2'

print(data_dict[key_name])

print(getattr(d2, key_name))

print(data_dict.get('key10', None))

print(getattr(d2, 'key10', None))

print(data_dict['key1'])

print(d2.key1)

data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

keys = set()

for d in data_list:
    for key in d.keys():
        keys.add(key)

print(keys)

keys = {key for dict_ in data_list for key in dict_.keys()}

print(keys)

Struct = namedtuple('Struct', sorted(keys))

print(Struct._fields)

Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)

data_list = [
    {'key2': 2, 'key1': 1},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

tuple_list = []

for dict_ in data_list:
    tuple_list.append(Struct(**dict_))

print(tuple_list)

def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', keys, rename = True)
    Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

tuple_list = tuplify_dicts(data_list)

print(tuple_list)