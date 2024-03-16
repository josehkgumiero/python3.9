class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

from collections import namedtuple

Point2D = namedtuple('Point2D', ['x', 'y'])

pt1 = Point2D(10, 20)

print(pt1)

pt3d_1 = Point3D(10, 20, 30)

print(
    pt3d_1
)

Pt2D = namedtuple('Point2D', ('x', 'y'))

pt1 = Point2D(10, 20)

print(pt1)

pt3d_1 = Point3D(10, 20, 30)

print(
    pt3d_1
)

Pt2D = namedtuple('Point2D', ('x', 'y'))

pt2 = Point2D(10, 20)

print(pt2)

Pt3D = Point3D

p = Pt3D(10, 20, 30)

print(p)

p = Point3D(x = 10, y = 20, z = 30)

print(
    p.x
)

print(
    p.y
)

p = Point2D(x = 10, y = 20)


print(p)

print(
    isinstance(p, tuple)
)

p = Point3D(x = 10, y = 20, z = 30)

print(
    isinstance(p, tuple)
)

a = (10, 20)

b = (10, 20)

print(
    a is b
)

print(
    a == b
)

pt1 = Point2D(10, 20)
pt2 = Point2D(10, 20)

print(
    pt1 is pt2,
    pt1 == pt2
)

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'
    
    def __eq__(self, other):
        if isinstance(other,Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.x
        else:
            return False

pt1 = Point3D(10, 20, 30)

pt2 = Point3D(10, 20, 30)

print(
    pt1,
    pt1 == pt2,
)

pt1 = Point2D(10, 20)

pt2 = Point3D(10, 20, 30)

print(max(pt1))

try:
    print(max(pt2))
except Exception:
    print(Exception)

def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

pt1 = Point3D(1, 2, 3)

pt2 = Point3D(1, 1, 1)

dot_product_3d(pt1, pt2)

a = (1, 2)

b = (1, 1)

print(
    list(zip(a, b))
)

print(
    sum(e[0] * e[1] for e in zip(a, b))
)

def dot_product(a, b):
    return sum(e[0] * e[1] for e in zip(a, b))

print(
    dot_product(a, b)
)

pt1 = Point2D(1, 2)

pt2 = Point2D(1, 1)

dot_product(pt1, pt2)

Vector3D = namedtuple('Vector3D', 'x y z')

v1 = Vector3D(1, 2, 3)

v2 = Vector3D(1, 1, 1)

print(v1)

print(tuple(v1))

print(v1[0])

print(v1[0:2])

print(v1)

print(v1.x)

print(v1.y)

Circle = namedtuple('Circle', 'center_x center_y  radius')

c = Circle(0, 0, 10)

print(c)

print(c.radius)

Stock = namedtuple('Stock', '''Symbol 
                   year 
                   month 
                   day 
                   open 
                   high 
                   low 
                   close''')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_383)

print(djia)

print(djia.close)

for item in djia:
    print(item)

p = Point2D(10, 20)

x, y = p

print(x, y)

print(djia)

symbol, year, month, day, *_, close = djia

print(symbol, year, month, day, close)

print(_)

Person = namedtuple('Person', 'name age _ssn', rename = True)

print(Person._fields)

print(Point2D._fields)

print(Stock._fields)

print(Point2D._source)

print(djia)

d = djia._asdict()

print(d['symbol'])

print(d['close'])

print(djia._asdict())

print(dict(djia._asdict()))