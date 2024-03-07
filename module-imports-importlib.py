import sys

print(sys)

import collections

print(collections)

mod_name = 'math'

import importlib

print(importlib)

print(importlib.import_module(mod_name))

print('math' in sys.modules)

print('fractions' in sys.modules)

print('math' in globals())

math2 = importlib.import_module(mod_name)

print(math2)

print('math2' in globals())

print(id(math2))

print(id(sys.modules['math']))

print(math2.sqrt(2))

print(math2)

print(importlib)

fractions = importlib.import_module('fractions')

print(fractions)

print(fractions.__spec__)

print(sys.meta_path)

import math

print(math.__spec__)

print(importlib.util.find_spec('decimal'))

with open('module-application-2.py', 'w') as code_file:
    code_file.write("print('running module-application-2...')\n")
    code_file.write('a=100\n')

mdl = importlib.util.find_spec('module-application-2')

print(mdl)

print('module-application-2' in globals())

mdl2 = importlib.import_module('module-application-2')

print(mdl2)

import os

getcwd = os.getcwd()

ext_module_path = ''

print(ext_module_path)

file_abs_path = os.path.join(ext_module_path, 'module-application-3.py')

with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module-application-3.py...')\n")
    code_file.write("x = 'python'\n")

mdl3 = importlib.util.find_spec("module-appliction-3")

print(sys.path)

print(sys.path.append(ext_module_path))

mdl4 = importlib.util.find_spec("module-appliction-3")

mdl4 = importlib.import_module('module-application-3')

print(mdl4.x)

