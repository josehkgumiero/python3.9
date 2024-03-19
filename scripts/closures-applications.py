class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

a = Averager()

print(
    a.add(10),
    a.add(20),
    a.add(30)
)

def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager()

print(
    a(10),
    a(20),
    a(30)
)

def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total / count
    return add

a = averager()

print(
    a.__closure__,
    a.__code__.co_freevars
)

from time import perf_counter

print(
    perf_counter(),
    perf_counter()
)

class Timer:
    def __init__(self):
        self.start = perf_counter()
    def poll(self):
        return perf_counter() - self.start

t1 = Timer()

print(
    t1.poll()
)

def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()

print(
    t2(),
    t2()
)

def counter(initial_value = 0):
    def inc(increment = 1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter1 = counter()

print(
    counter1(),
    counter1()
)

def counter(f):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(
            '{0} has been called {1} times' \
            .format(f.__name__, cnt)
        )
        return f(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

counter_add = counter(add)

print(
    counter_add.__closure__,
    counter_add.__code__.co_freevars
)

result = counter_add(10, 20)

print(result)

counter_mult = counter(mult)

print(
    counter_mult(2, 5)
)

counters = dict()

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

counted_add = counter(add)

counted_mult = counter(mult)

def counter(fn, counters):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

d = dict()

counted_add = counter(add, d)

counter_mult = counter(mult, d)

print(counters)

print(
    counted_add(10, 20),
    counted_mult(2, 5),
    counted_mult(3, 6),
    counters,
    d
)

def fact(n):
    product = 1
    for i in range(2, n+ 1):
        product *= i
    return product

print(
    fact(3),
    fact(5)
)

counted_fact = counter(fact, d)

print(
    counted_fact(5)
)

fact = counter(fact, d)

print(
    fact.__closure__
)

print(
    fact(3),
    fact(5),
    d
)