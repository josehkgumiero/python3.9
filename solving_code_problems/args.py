a, b, *c = 10, 20, 'a', 'b'

print(
    a,
    b,
    *c
)

def f1(a, b, *c):
    print(
        a,
        b,
        *c
    )

f1(10, 20)

f1(10, 20, 1, 2, 3)

def avg(*args):
    print(args)

print(
    avg()
)

avg(10, 20)

def avg(*args):
    try:
        count = len(args)
        total = sum(args)
        return total / count
    except Exception:
        print(Exception)

print(
    avg()
)

def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count

print(
    avg(
        2,
        2,
        4,
        4
    )
)

def f1(a, b, c):
    print(
        a,
        b,
        c
    )

l = [10, 20, 30]

f1(*l)