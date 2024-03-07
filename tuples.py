print(
    (10, 20, 30)
)

a = (10, 20, 30)

b = 10, 20, 30

print(
    type(a)
)

print(
    type(b)
)

def print_tuple(t):
    for e in t:
        print(e)

print_tuple((10, 20, 30))

a = 'a', 10, 200

print(a[0])

print(a[1])

b = 1, 2, 3, 4, 5, 6

print(
    type(b)
)

print(
    a[2:5]
)

for e in a:
    print(e)

a = 'a', 10, 20

x, y, z = a

print(x, z)

c = 1, 2, 3, 4, 5

x, *other, y, z = a

print(x, y, z, other)

x, *_, y, z = a

print(x, y, z, _)

class Point2D:

    def __init__(self, x, y):
        self.x= x
        self.y = y
    
    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

pt = Point2D(10, 20)

print(
    pt
)

pt.x = 100

print(
    id(pt)
)

a = Point2D(0, 0), Point2D(10, 20)

print(a)

print(
    id(a[0])
)

a[0].x = 100

print(
    a
)

s = 'python'

print(
    id(s)
)

s = 'python' + ' rocks!'

print(s)

a = 1, 2, 3

a += (4, 5)

print(a)

print(id(a))

a = a + (4, 5)

pt1 = (0, 0)

pt2 = (10, 20)

london = 'London', 'UK', 8_700_000

new_york = 'New York', 'USA', 8_500_000

beijing = 'Beijing', 'China', 21_000_000

print(london)

cities = [london, new_york, beijing]

total = 0

for city in cities:
    total += city[2]
print(total)

total = sum(city[2] for city in cities)

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072

symbol, yer, month, day, open_, high, low, close = record

print(
    symbol,
    close
)

for city, country, population in cities:
    print(city, country, population)

for index, city in enumerate(cities):
    print(index, city)

from random import uniform

from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    
    return random_x, random_y, is_in_circle

num_attempts = 100

count_inside = 0

for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately: {4 * count_inside / num_attempts}')