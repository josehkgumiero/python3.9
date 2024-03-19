a = 10

def f(n):
    print('global a:', a)
    c = a ** n
    return c

print(
    f(2)
)

def f(n):
    a = 20
    print('local a:', a)
    c = a ** n
    return c

print(
    f(2)
)

def f(n):
    global a
    a = 20
    c = a ** n
    return c

print(
    a,
    f(2),
    a
)

def f():
    try:
        global v
        v = 'Hello World'
        return
    except Exception:
        print(Exception)

f()

print(v)

def f():
    global a
    a = 'Hello'
    print('global a:', a)

a = 10

print(a)

f()

print(a)

b = 10

def f():
    print('global a:', a)
    a = 'Hello world'
    print(a)

f = lambda n: print(b**n)

print(
    f(2)
)

print(
    True
)

def print(x):
    return 'Hello {0}'.format(x)

print('World')

del print

print('world')

for i in range(10):
    x = 2 * i

print(i)