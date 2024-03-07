from functools import partial

def _function(a, b, c):
    print(a, b, c)

print(
    _function(10, 20, 30)
)

def f(_a, _b):
    return _function(10, _a, _b)

print(
    f(20, 30)
)

print(
    f(100, 200)
)

_f = lambda _c, _d: _function(10, _c, _d)

print(
    _f(100, 200)
)

_f1 = partial(_function, 10)

print(
    _f1(20, 30)
)

_f2 = partial(_function, 10, 20)

print(
    _f2(20)
)

def _function1(_a, _b, *args, _k1, _k2, **kwargs):
    print(_a, _b, args, _k1, _k2, kwargs)

print(
    _function1(10, 20, 100, 200, _k1='a', _k2='b', _k3=1000, _k4=2000)
)

def _function2(_a, *vars, _kw, **kwvars):
    return _function1(10, _a, *vars, _k1='a', _k2=_kw, **kwvars)

print(
    _function2(20, 100, 200, _kw='b', _k3=1000, _k4=2000)
)

_function_partial = partial(_function1, 10, _k1='a')

print(
    _function_partial(20, 100, 200, _k2='b', _k3=1000, _k4=2000)
)

def pow(base, exponent):
    return base ** exponent

sq = partial(pow, exponent = 2)

print(
    sq
)

cu = partial(pow, exponent = 3)

print(
    cu
)

print(
    cu(5)
)

print(
    cu(base = 5)
)

print(
    cu(5, exponent = 2)
)

a = 2

_pow = partial(pow, exponent = a)

print(_pow(5))

a = 3

print(_pow(3))

def _function(a, b):
    print(a, b)

a = [1, 2]

_f1 = partial(_function, a)

print(
    _f1
)

print(
    a.append(3)
)

print(
    a
)

print(
    _f1(100)
)

origin = (0, 0)

_l1 = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]

_d1 = lambda a, b: (a[0] - b[0]**2 + (a[1] - b[1]**2))

print(
    _d1((1, 1), origin)
)

print(
    sorted(_l1)
)

_function = partial(_d1, origin)

print(
    _function((1, 1))
)

print(
    sorted(_l1, key = _function)
)

_lambda = lambda x: _d1(origin, x)

print(
    sorted(_l1, key = _lambda)
)

print(
    sorted(_l1, key = lambda x: _d1(origin, x))
)