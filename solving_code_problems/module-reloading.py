import os

def create_module_file(module_name, **kwargs):
    
    '''
    Create a module file named <mdule_name>.py
    Module has a single function (print_values) that will print
    out the suppliked (stringified) kwargs.
    '''

    module_file_name = f'{module_name}.py'

    module_rel_file_path = module_file_name

    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')

        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")

print(create_module_file('test', k1 = 10, k2 = 'python'))

import importlib

test = importlib.import_module('test')

print(test.print_values())

print(create_module_file('test', k1 = 10, k2 = 'python', k3 = 'cheese'))

test = importlib.import_module('test')

print(test.print_values())

print(id(test))

import sys

print('test' in sys.modules)

del sys.modules['test']

print('test' in sys.modules)

test = importlib.import_module('test')

print(id(sys.modules['test']))

print('test' in globals())

print(id(test))

print(test.print_values())

print(id(test), id(sys.modules['test']))

create_module_file('test', k = 10, k2 = 'python', k3 = 'cheese', k4 = 'parrots')

print(
    importlib.reload(test)
)

print(id(test))

print(id(sys.modules['test']))

print(test.print_values())

create_module_file('test2', k1 = 'python')

test2 = importlib.import_module('test2')

print(
    'test2' in globals()
)

print(
    'test' in sys.modules
)

print(
    test2.print_values
)

print(
    test2.print_values()
)

create_module_file('test2', k1 = 'python', k2 = 'cheese')

test2 = importlib.reload(sys.modules['test2'])

print(
    test2.print_values()
)

print_values = sys.modules['test2'].print_values

print(
    print_values()
)