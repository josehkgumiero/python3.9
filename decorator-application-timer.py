def timed(fn):

    from time import perf_counter

    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print(
            '{0}({1}) took {2:.6f}s to run.' \
            .format(
                fn.__name__,
                args_str,
                elapsed
            )
        )

        return result
    
    return inner

@timed
def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        calc_recursive_fib(n - 1) + calc_recursive_fib(n - 2)

print(
    calc_recursive_fib(3)
)

@timed
def fib_recursive(n):
    return calc_recursive_fib(n)

print(
    fib_recursive(3)
)

@timed
def fib_loop(n):
    f1 = 1
    f2 = 1
    for i in range(3, n + 1):
        f1, f2 = f2, f1 + f2
    return f2

print(
    fib_loop(36)
)

from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(
        lambda prev, n: (prev[0] + prev[1], prev[0]),
        dummy,
        initial
    )
    return fib_n[0]

print(
    fib_reduce(35)
)