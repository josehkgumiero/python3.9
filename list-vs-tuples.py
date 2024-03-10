# List vs Tuples

from dis import dis

t = (1, 2, 3)

l = [1, 2, 3]

print("\n")

dis(compile('(1, 2, 3, "a")', 'string', 'eval'))

print("\n")

dis(compile('[1, 2, 3, "a"]', 'string', 'eval'))

print("\n")

dis(compile('(1, 2, 3, [10, 20])', 'string', 'eval'))

print("\n")

from timeit import timeit

print("\n")

print(
    timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number = 10_000_000)
)

print("\n")

print(
    timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number = 10_000_000)
)

def fn1():
    pass

print("\n")

dis(compile('(fn1, 10, 20)', 'string', 'eval'))

print("\n")

dis(compile('(1, 2, 3, [10, 20])', 'string', 'eval'))

print("\n")

dis(compile('[1, 2, 3, [10, 20]]', 'string', 'eval'))

print("\n")

print(
    timeit("([1, 2], 10, 20)", number = 1_000_000)
)

print("\n")

print(
    timeit("[[1, 2], 10, 20]", number = 1_000_000)
)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print("\n")

print(
    id(l1),
    id(t1)
)

l2 = list(l1)

print("\n")

print(id(l2))

t2 = tuple(t1)

print("\n")

print(id(t2))

print("\n")

print(
    timeit("tuple((1, 2, 3, 4, 5))", number = 5_000_000)
)

print("\n")

print(
    timeit("list((1, 2, 3, 4, 5))", number = 5_000_000)
)