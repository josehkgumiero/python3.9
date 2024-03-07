_l = [5, 8, 6, 10, 9]

_max = lambda x, y: x if x > y else y

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(
    max_sequence(_l)
)

_min = lambda a, b: a if a < b else b

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result

print(
    min_sequence(_l)
)

_add = lambda a, b: a + b

def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result

print(
    add_sequence(_l)
)

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

print(
    _reduce(_max, _l)
)

from functools import reduce

reduce(_max, _l)

reduce(_add, _l)

reduce(_max, {1, 3, 4, 5})

print(
    min(_l)
)

print(
    min({1, 2, 3})
)

print(
    max(_l)
)

print(
    sum({1, 2, 3})
)

_s = {True, 1, 0, None}

print(
    all(_s)
)

_s2 = {True, 1, 's'}

print(
    all(_s2)
)

print(
    bool(True) and bool(1) and bool('s')
)

print(
    any(s)
)

print(
    any(_s2)
)

_s3 = {False, 0, '', None}

print(
    any(_s3)
)

_t1 = reduce(lambda a, b: bool(a) and bool(b), _s)

print(_t1)

_t2 = reduce(lambda a, b: bool(a) or bool(b), _s3)

print(_t2)

_l1 = [5, 8, 6, 10, 9]

print(_l1)

_t3 = reduce(lambda a, b: a* b, _l1)

print(_t3)

print(
    range(5)
)

print(
    range(5)[0]
)

print(
    list(range(5))
)

print(
    list(range(range(1, 5 + 1)))
)

print(
    reduce(lambda a, b: a *b, range(1, 5 + 1))
)

def fact(n):
    return 1 if n < 2 else n * fact(n - 1)

print(
    fact(5)
)

def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

print(
    fact(5)
)

def _reduce(fn, sequence, initial):
    result = initial
    for x in sequence:
        result = fn(result, x)
    return result

_r1 = _reduce(lambda a, b: a + b, _l1, 100)

print(_r1)

_r2 = _reduce(lambda a, b: a + b, {1, 2, 3, 4}, 0)

print(_r2)