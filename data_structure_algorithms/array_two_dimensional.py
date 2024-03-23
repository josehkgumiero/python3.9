# python ./data_structure_algorithms/two_dimensional_array.py

import numpy as np

_two_array = np.array(
    [
        [11, 15, 10, 6],
        [10, 14, 11, 5],
        [12, 17, 12, 8],
        [15, 18, 14, 9]
    ]
)

print("\n")

print(_two_array)

_new_two_array = np.insert(
    _two_array,
    0,
    [[1, 2, 3, 4]],
    axis = 0
)

print("\n")

print(_new_two_array)

_new_two_array = np.insert(
    _two_array,
    1,
    [[1, 2, 3, 4]],
    axis = 0
)

print("\n")

print(_new_two_array)

_new_two_array = np.append(
    _two_array,
    [[1, 2, 3, 4]],
    axis = 0
)

print("\n")

print(_new_two_array)

def access_elements(_array, _row_index, _col_index):
    if _row_index >= len(_array) and _col_index >= len(_array[0]):
        print("Incorect index")
    else:
        print(_array[_row_index][_col_index])

print("\n")

access_elements(_new_two_array, 1, 1)

def traverse_array(_array):
    for i in range(len(_array)):
        for j in range(len(_array[0])):
            print(_array[i][j])
        print("\n")

print("\n")

traverse_array(_new_two_array)

def search_array(_array, _value):
    for i in range(len(_array)):
        for j in range(len(_array[0])):
            if _array[i][j] == _value:
                return "The value is located at index " + str(i) + " " + str(j)
    return 'The element is not found'

print("\n")

print(search_array(_new_two_array, 55))


print("\n")
print(_new_two_array)
_new_array = np.delete(_new_two_array, 0 , axis = 0)
print("\n")
print(_new_array)