def func():
    a = 10
    return a

print(func)

print(func())

print(id(func))

print(globals())

f = globals()['func']()

print(f)

print(f is func)

print(locals() is globals())

def func():
    a = 10
    b = 10
    print(locals())

print(func())

import math

print(math)

import fractions

print(fractions)

junk = math

print(junk.sqrt(2))

print(junk is math)

print(globals())

print(
    globals()['math']
)

mod_math = globals()['math']

print(mod_math.sqrt(2))

print(type(globals()))

print(type(math))

print(type(fractions))

print(id(math))

import sys

print(type(sys.modules))

print(sys.modules['math'])

print(id(sys.modules['math']))

print(math.__name__)

print(math.__dict__)

f = math.__dict__['sqrt']

print(f)

print(f(2))

import fractions

print(sys.modules['fractions'])

print(dir(fractions))

print(fractions.__dict__)

import calendar

print(calendar)

import types

print(isinstance(fractions, types.ModuleType))

print(isinstance(math, types.ModuleType))

mod = types.ModuleType('test', 'THis is a test module')

from types import ModuleType

print(isinstance(mod, ModuleType))

print(mod.__dict__)

mod.pi = 3.14

print(mod.__dict__)

mod.hello = lambda: 'Hello!'

print(mod.hello())

hello = mod.hello

print('hello' in globals())

from collections import namedtuple

mod.Point = namedtuple('Point', 'x y')

p1 = mod.Point(0, 0)

p2 = mod.Point(1, 1)

print(p1)

print(dir(mod))

PT = getattr(mod, 'Point')

print(PT(20, 20))

PT = mod.__dict__['Point']

print(PT)