def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()

print(
    outer_func()
)

def outer_func():
    x = 'Hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

print(
    outer_func()
)

def outer_func():
    a = 'Hello'
    def inner():
        a = 'python'
        print('inner:', a)
    inner()
    print('outer:', a)

print(
    outer_func()
)

def outer_func():
    a = 'Hello'
    def inner():
        nonlocal a
        a = 'python'
        print('inner:', a)
    print('outer(before):', a)
    inner()
    print('outer(after):', a)

outer_func()

def outer():
    a = 'Hello'
    def inner1():
        def inner2():
            nonlocal a
            a = 'python'
        inner2()
    inner1()
    print(a)

outer()

def outer():
    a = 'Hello'
    def inner1():
        nonlocal a
        a = 'Python'
        def inner2():
            nonlocal a
            a = 'Monty'
        inner2()
    inner1()
    print(a)

outer()

def outer():
    global a
    a = 'Monty'

    def inner():
        global a
        a = 'Hello'

    inner()

    print(a)

outer()

print(a)