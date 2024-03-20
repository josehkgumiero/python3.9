def fib(n):
    print(
        'Calculating fib({0})'\
        .format(n)
    )
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

print(
    fib(10)
)

class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print(
                'Calculating fib({0})' \
                .format(n)
            )
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

f = Fib()

print(
    f.fib(10)
)

def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib

f = fib()

print(
    f(10)
)

g = fib()

print(
    g(10)
)

def memorize_fib(fib):
    cache = {1: 1, 2: 1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]
    
    return inner

@memorize_fib
def fib(n):
    print(
        'Calculating fib({0})' \
        .format(n)
    )
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))

def fact(n):
    print(
        'Calculting {0}!' \
        .format(n)
    )
    return 1 if n < 2 else n * fact(n-1)

print(fact(6))

def memorize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@memorize
def fib(n):
    print(
        'Calculating fib({0})' \
        .format(n)
    )
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))