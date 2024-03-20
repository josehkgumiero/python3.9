def outer():
    a ='python'
    def inner():
        print(a)
    return inner

f = outer()

print(
    f.__code__.co_freevars
)

print(
    f.__closure__
)

print(
    f.__closure__
)

def outer():
    a = [1, 2, 3]
    print(
        hex(
            id(a)
        )
    )
    def inner():
        a = [1, 2, 3]
        print(
            hex(
                id(
                    a
                )
            )
        )
    return inner

f = outer()

print(f.__closure__)

print(f())

def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

f = outer()

print(
    f.__code__.co_freevars
)

print(
    f.__closure__
)

print(
    hex(
        id(
            0
        )
    )
)

print(
    f()
)

def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return 1
    
    def inc2():
        nonlocal count
        count += 1
        return count
    
    return inc1, inc2

f1, f2 = outer()

print(
    f1.__code__.co_freevars,
    f2.__code__.co_freevars
)

print(
    f1.__closure__,
    f2.__closure__
)

print(
    f1(),
    f2()
)

def pow(n):
    def inner(x):
        return x**n
    return inner

s = pow(2)

print(
    s.__closure__,
    hex(id(2)),
    s,
    s(5)
)

c = pow(3)

print(
    c.__closure__
)

def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)

add_2 = adder(2)

add_3 = adder(3)

print(
    add_1.__closure__,
    add_2.__closure__,
    add_3.__closure__,
    add_1(10),
    add_2(10),
    add_3(10)
)

adders = []

for n in range(1, 4):
    adders.append(lambda x: x + n)

print(
    adders,
    n,
    adders[0].__closure__,
    adders[0](10)
)

def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders

adders = create_adders()

print(
    adders
)

print(
    adders[0].__closure__,
    adders[1].__closure__
)