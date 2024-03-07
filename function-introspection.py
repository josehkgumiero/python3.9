def _function(
    a,
    b,
    c,
    *args
):
    a = 10
    b = 20

print(
    _function.__doc__
)

print(
    _function.__annotations__
)

_function.short_description = "THis is a function that does nothing much"

print(
    _function.short_description
)

print(
    dir(_function)
)

print(
    _function.__name__
)

def _function_call(f):
    print(id(f))
    print(f.__name__)

_function_call(_function)

print(
    _function.__defaults__
)

print(
    _function.__kwdefaults__
)

print(
    _function.__code__
)

print(
    _function.__code__.co_name
)

print(
    _function.__code__.co_varnames
)

print(
    _function.__code__.co_argcount
)

import inspect

from inspect import isfunction, ismethod, isroutine

a = 10

print(
    isfunction(a)
)

print(
    isfunction(_function)
)

print(
    ismethod(_function)
)

class MyClass:
    def f(self):
        pass

print(
    isfunction(MyClass.f)
)

my_object = MyClass()

print(
    isfunction(my_object.f)
)

print(
    ismethod(my_object.f)
)

print(
    isroutine(my_object.f)
)

print(
    isroutine(MyClass.f)
)

print(
    inspect.getsource(_function)
)

print(
    inspect.getmodule(_function)
)

print(
    inspect.getmodule(print)
)

