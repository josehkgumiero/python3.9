import sys

print(
    sys \
        .getsizeof(0)
)

print(
    sys \
        .getsizeof(1)
)

print(
    sys \
        .getsizeof(2**1000)
)

import time

def calc(a):
    for i \
        in range(10000000):
            a * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(
      end - start
)

start = time.perf_counter()
calc(2**1)
end = time.perf_counter()
print(
      end - start
)


