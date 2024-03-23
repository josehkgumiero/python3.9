import array

print("\n")
_array_1 = array.array('i')
print(_array_1)

print("\n")
_array_2 = array.array('i', [1, 2, 3, 4])
print(_array_2)

import numpy as np

print("\n")
_np_array_1 = np.array([], dtype=int)
print(_np_array_1)

print("\n")
_np_array_2 = np.array([1, 2, 3, 4])
print(_np_array_2)

print("\n")
_array_3 = array.array('i', [1, 2, 3, 4])
print(_array_3)
_array_3.insert(0, 6)
print(_array_3)

print("\n")
_array_4 = array.array('i', [1, 2, 3, 4, 5, 6])
_array_5 = array.array('d', [1.3, 1.5, 1.6])

def traverseArray(_array):
    for _index in _array:
        print(_index)

traverseArray(_array_4)
traverseArray(_array_5)

def accessElement(_array, _index):
    if _index >= len(_array):
        print("There is not any element in this index.")
    else:
        print(_array[_index])

accessElement(_array_4, 6)
accessElement(_array_4, 5)

def linear_search(_array, _target):
    for _index in range(len(_array)):
        if _array[_index] == _target:
            return _index
    return -1

print(linear_search(_array_4, 8))
print(linear_search(_array_4, 6))

_array_4.remove(6)

print(_array_4)

help(array)
# python ./data_structure_algorithms/array.py