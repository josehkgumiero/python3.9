# module-timing-run.py

import importlib

timing = importlib.import_module('module-timing')

code = '[x**2 for x in range(1_000_000)]'

result = timing.timeit(code, 100)

print(result)