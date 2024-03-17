import importlib.util
module_name = "unittest"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)
module_name = "venv"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)
module_name = "pytest"
print(module_name)
found = importlib.util.find_spec(module_name) is not None
print(found)

# python ./importlib_util_find_spec/__init__.py