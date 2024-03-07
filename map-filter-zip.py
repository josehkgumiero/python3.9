def fact(n):
    return 1 if n < 2 else n * fact(n - 1)

print(
    fact(3)
)

print(
    fact(4)
)

results = list(map(fact, range(6)))

print(results)

for x in results:
    print(x)

l1 = [1, 2, 3, 4, 5]

l2 = [10, 20, 30]

l3 = 100, 200, 300, 400

results = list(map(lambda x, y, z: x + y + z, l1, l2, l3))

print(results)

for x in results:
    print(x)

x = range(25)

print(x)

l = list(
    filter(
        lambda x: x% 3 == 0,
        range(25)
    )
)

l = list(
    filter(
        None,
        [1, 0, 4, 'a', '', None, True, False]
    )
)

l1 = [1, 2, 3, 4]

l2 = [10, 2, 30, 40]

l3 = 'python'

results = zip(l1, l2, l3)

for x in results:
    print(x)

results = [fact(n) for n in range(10)]

print(results)

results = (fact(n) for n in range(10))

print(results)

for x in results:
    print(x)

results = list((fact(n) for n in range(10)))

print(results)

l1 = [1, 2, 3, 4, 5, 6]

l2 = [10, 20, 30, 40]

results = list(map(lambda x, y: x+ y, l1, l2))

print(results)

results = [x + y for x, y in zip(l1, l2)]

print(results)

print(
    list(
        filter(
            lambda x: x% 2 == 0, map(lambda x, y: x + y, l1, l2)
        )
    )
)

print(
    [x + y for x, y in zip(l1, l2) if (x + y) % 2 == 0]
)

