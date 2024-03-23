# python ./data_structure_algorithms/one_dimensional_array.py

import array

# Creates an array
_array = array.array('i', [1, 2, 3, 4, 5])

# Traverse an array
print("\n")
for _index in _array:
    print(_index)

# Access individual elements through indexes
print("\n")
for _index in range(0, len(_array)):
    print(_array[_index])

# Append any value using append() method
print("\n")
_array.append(6)
print(_array)

# Insert vaue using insert() method
print("\n")
_array.insert(6, 7)
print(_array)

# Extend the array using extend() method
print("\n")
_other_array = [10, 11, 12]
_array.extend(_other_array)
print(_array)

# From list add to array
print("\n")
_list = [20, 21, 22]
_array.fromlist(_list)
print(_array)

# Remove a item of array by the index
print("\n")
print("Length of the array:", int(len(_array)))
print("Array: ", _array)
_array.remove(5)
print("Array: ", _array)

# Remove the last index of array using pop() method
print("\n")
print(_array)
_array.pop()
print(_array)

# Fetch the element by index
print("\n")
print(_array)
print(_array.index(6))

# Reverse a python array using reverse() method
print("\n")
print(_array)
_array.reverse()
print(_array)

# Get array buffer information
print("\n")
print(_array.buffer_info())

# Get the number of occurrences of an element using the count() method
print("\n")
_array.append(11)
_array.append(11)
print(_array)
print(_array.count(11))

# Convert the array to string using tostring() method
print("\n")
_str_array = str(_array)
print(_str_array)

# Convert array to list
print("\n")
print(_array)
_list = _array.tolist()
print(_list)