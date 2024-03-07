from decimal \
import Decimal

a = 3.1415

import sys

print(
    sys.getsizeof(a)
)

b = Decimal('3.1415')

print(
    sys.getsizeof(b)
)

import time

def run_float(n = 1):
    for i \
        in range(n):
            c = 3.1415

def run_decimal(n = 1):
    for i \
        in range(n):
            d = Decimal('3.1415')

n = 10000000

start = \
    time.perf_counter()
run_float(n)
end = \
    time.perf_counter()
print(
    '''
    float: {0}
    ''' \
    .format(end - start)
)

start = \
    time.perf_counter()
run_decimal(n)
end = \
    time.perf_counter()
print(
    '''
    float: {0}
    ''' \
    .format(end - start)
)