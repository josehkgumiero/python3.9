def f1(a, b, c):
    print(a, b, c)

f1(1, 2, 3)

f1(1, c = 3, b = 2)

f1(c = 3, b =2, a = 1)

def f2(a, b, *args):
    print(a, b, args)

f2(1, 2, 3, 4)

def f3(a, b, *args, d):
    print(a, b, args, d)

f3(1, 2, 3, 4, d = 5)

def f4(*args, d):
    print(args, d)

f4(1, 2, 3, d = 'a')

f4(d = 'a')

def f5(*, d):
    print(d)

f5(d = 100)

def f6(a, b, *, d):
    print(a, b, d)

f6(1, 2, d = 4)

def f7(a, b = 2, *args, d):
    print(a, b, args, d)

f7(1, 5, 3, 4, d = 'a')

def f8(a, b = 20, *args, d= 0, e):
    print(a, b, args, d, e)

f8(5, 4, 3, 2, 1, e = 'all engines running')

f8(0, 600, d = 'good morning', e = 'python')

f8(11, 'n/s', 24, 'mph', d = 'unladen', e = 'swallow')

