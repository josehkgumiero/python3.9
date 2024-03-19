def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(
            'Function {0} was called {1} times' \
            .format(fn.__name__, count)
        )
        return fn(*args, **kwargs)
    return inner

def add(a: int, b: int = 0):
    """
    adds two values
    """
    return a + b

# help(add)

print(
    add(10, 20),
    add(20, 40),
    add(10)
)

def mult(a: int, b: int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

print(
    mult(1, 2, 3, d = 4)
)

print(
    mult(1, 2, d = 3)
)

mult = counter(mult)

# help(mult)

@counter
def fn(s: str, i: int) -> str:
    return s * i

# help(fn)

print(
    fn('a', 10)
)