import sys

import importlib

module_application_1 = importlib.import_module("module-application-1")

print('==================')

print('Runing main.py - module name: {0}'.format(__name__))

print(module_application_1)

module_application_1.pprint_dict('main.globals', globals())

print('=================')