print("\n")

t = tuple()
import sys
prev = sys.getsizeof(t)
for i in range(10):
    c = tuple(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta = {delta}')

print("\n")

l = list()
import sys
prev = sys.getsizeof(t)
for i in range(10):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta = {delta}')

print("\n")

c = list()
prev = sys.getsizeof(c)
print(f'0 items: {prev}')
for i in range(255):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta = {delta}')

t = tuple(range(100_000))

l = list(t)

from timeit import timeit

print(
    timeit('t[99_999]', globals = globals(), number = 10_000_000)
)