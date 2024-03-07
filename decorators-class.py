def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwarg):
            print(
                """
                Decorated function called: a ={0}, b={1}
                """.format(a, b)
            )
            return fn(*args, **kwarg)
        return inner
    return dec

@my_dec(10, 20)
def my_func(s):
    print(
        """
        Hello {0}
        """.format(s)
    )

print(
    my_func("World")
)

class MyClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __call__(self, c):
        print(
            "Called a={0}, b={1}, c={2}".format(self.a, self.b, c)
        )

o = MyClass(10, 20)

print(o)

print(o.__call__)

print(o(100))

class MyClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __call__(self, fn):
        def inner(*args, **kwarg):
            print(
                """
                DEcorated function called: a={0}, b={1}
                """.format(self.a, self.b)
            )
            return fn(*args, **kwarg)
        return inner

@MyClass(10, 20)
def my_func(s):
    print(
        """
        Hello {0}
        """.format(s)
    )

print(
    my_func("World")
)

o = MyClass(10, 20)

def my_func(s):
    print(
        "Hello {0}".format(s)
    )

my_func = o(my_func)

print(
    my_func("World")
)