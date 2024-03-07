def sq(x):
    return x**2

print(
    type(
        sq
    )
)

print(
    sq
)

_lx = lambda x: x**2

print(_lx)

_lx_a = lambda a, b: a + b

print(
    _lx_a
)

_f = _lx_a

print(
    id(_f),
    id(sq)
)

_a = lambda x, *args, y, **kwargs: (x, *args,y, kwargs)

print(
    _a(1, 'a', 'b', y = 100, a = 10, b = 20)
)

def apply_func(x, fn):
    fn(x)

apply_func(5, sq)

apply_func(5, lambda x: x**2)

apply_func(5, lambda x: x**3)

def _apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

_apply_func(sq, 3)

_apply_func(lambda x: x**2, 3)

_apply_func(lambda x, y: x + y, 1, 2)

_apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5)

_apply_func(sum, (1, 2, 3, 4, 5))