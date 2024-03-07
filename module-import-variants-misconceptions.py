import sys

for key in sorted(sys.modules.keys()):
    print(key)

print('cmath' in sys.modules)

print('cmath' in globals())

from cmath import exp

print('cmath' in globals())

print('exp' in globals())

print(exp)

print(id(exp))

print('cmath' in sys.modules)

print(exp(2+2j))

cmath = sys.modules['cmath']

print('cmath' in globals())

print(cmath.exp(2+2j))

print(cmath.sin(2+2j))

print(cmath.pi)

print(cmath.cos(2+2j))

from cmath import *

print(globals())

print(sin(2+2j))

from cmath import sin as c_sin

print(c_sin)

from math import sin as r_sin

print(r_sin)

def f(a):
    import math
    return math.sqrt(a)

from time import perf_counter

from collections import namedtuple

Timings = namedtuple('Timings', 'timing_1m timing_2, abs_diff rel_diff_perc')

def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1) / timing1 * 100

    timings = Timings(
        round(timing1, 1),
        round(timing2, 1),
        round(timing2 - timing1, 1),
        round(rel_diff, 2)
    )

    return timings

print(
    compare_timings(1, 2)
)

test_repeats = 10_000_000

import math

start = perf_counter()

for _ in range(test_repeats):
    math.sqrt(2)

end = perf_counter()

elapsed_fully_qualified = end - start

print(f'Elapsed: {elapsed_fully_qualified}')

start = perf_counter()

for _ in range(test_repeats):
    math.sqrt(2)

end = perf_counter()

elapsed_direct_symbol = end - start

print(f'Elapsed: {elapsed_direct_symbol}')

print(
    compare_timings(
        elapsed_fully_qualified,
        elapsed_direct_symbol
    )
)

def func():
    math.sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_func_fully_qualified = end - start

print(f'Elapsed: {elapsed_func_fully_qualified}')

from math import sqrt

def func():
    sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_func_direct_symbol = end - start

print(f'Elapsed: {elapsed_func_direct_symbol}')

print(
    compare_timings(
        elapsed_func_fully_qualified,
        elapsed_func_direct_symbol
    )
)

def func():
    import math
    math.sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_nested_fully_qualified = end - start

print(f'Elapsed: {elapsed_nested_fully_qualified}')

def func():
    from math import sqrt
    sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_nested_direct_symbol = end - start

print(f'Elapsed: {elapsed_nested_direct_symbol}')