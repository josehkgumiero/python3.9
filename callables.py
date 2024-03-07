print(
    callable(print)
)

l = [1, 2, 3]

print(
    callable(l.append)
)

s = 'abc'

print(
    callable(
        s.upper()
    )
)

from decimal import Decimal

print(
    callable(
        Decimal
    )
)

a = Decimal('10.5')

print(
    a
)

class MyClass:
    def __init__(self, x = 0):
        print('Initializing...')
        self.counter = x
    def __call__(self, x = 1):
        print('Updating counter...')
        self.counter = x

print(
    callable(
        MyClass
    )
)

b = MyClass(100)

print(
    b.counter
)

print(
    callable(
        b
    )
)

print(
    MyClass.__call__(b, 10)
)

print(
    b.counter
)

print(
    callable(b)
)