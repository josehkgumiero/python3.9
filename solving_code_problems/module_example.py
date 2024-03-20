import operator

print(
    dir(operator)
)

print(
    operator.add(1, 2),
    operator.mul(2, 3),
    operator.truediv(3, 2),
    operator.floordiv(13, 2)
)

print(
    13 // 2
)

from functools import reduce

print(
    reduce(lambda x, y: x * y, [1, 2, 3, 4]),
    reduce(operator.mul, [1, 2, 3, 4]),
    operator.lt(10, 3)
)

from operator import is_

print(
    is_('abc', 'def'),
    is_('abc', 'abc'),
    operator.truth([]),
    operator.truth([1])
)

_l1 = [1, 2, 3, 4]

print(
    _l1[1],
    operator.getitem(_l1, 1)
)

_l1[1] = 100

print(
    _l1
)

del _l1[3]

print(
    _l1
)

_l2 = [1, 2, 3, 4]

print(
    operator.setitem(_l2, 1, 100),
    _l2,
    operator.delitem(_l2, 3),
    _l2,
    operator.itemgetter(2),
    type(operator.itemgetter(2))
)

_l3 = [1, 2, 3, 4]

print(
    operator.itemgetter(_l3),
    operator.itemgetter('python'),
    operator.itemgetter(2, 3, 4),
    type(operator.itemgetter)
)

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')

_o = MyClass()

print(_o)

print(_o.a)

print(_o.b)

print(
    _o.test()
)

_pa = operator.attrgetter('a')

print(_pa(_o))

_var = 'b'

_pb = operator.attrgetter(_var)

print(_pb(_o))

_var = 'c'

print(_pb(_o))

a, b, test = operator.attrgetter('a', 'b', 'test')(_o)

print(
    a,
    b,
    test,
    test()
)

_f1 = lambda x: x.a

print(_f1(_o))

_f2 = lambda x: (x[2], x[3])

_l1 = [1, 2, 3, 4]

print(_f2(_l1))

_a = 5 + 10j

print(
    _a,
    _a.real
)

_l2 = [5 - 10j, 3 + 3j, 2-100j]

print(
    sorted(_l2, key = operator.attrgetter('real'))
)

_l3 = [(2, 3, 4), (1, 3, 5), (6,), (4, 100)]

_f3 = sorted(_l3, key = lambda x: x[0])

print(_f3)

_f4 = sorted(_l3, key = operator.itemgetter(0))

print(_f4)

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self, c, d, *, e):
        print(self.a, self.b, c, d, e)

_o = MyClass()

print(
    _o.a,
    _o.b,
    _o.test(100, 200, e = 300),
    operator.methodcaller('test', 100, 200, e = 300)(_o),
    operator.attrgetter('test')
)