import importlib.util

print("\n")
module_name = "unittest"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)

print("\n")
module_name = "venv"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)

print("\n")
module_name = "pytest"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)

print("\n")
module_name = "array"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)

print("\n")
module_name = "numpy"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)

print("\n")
module_name = "pprint"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)

# python ./importlib_util_find_spec/app.py