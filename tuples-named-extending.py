from collections import namedtuple

Point2D = namedtuple('POint2D', 'x y')

pt = Point2D(10, 20)

print(pt)

print(pt[0])

print(pt.x)

pt.x = 100

pt[0] = 100

print(id(pt))

pt = Point2D(100, pt.y)

print(pt)

print(id(pt))

s = 'python'

print(id(s))

s += ' rocks!'

print(s)

print(id(s))

Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 28_260, 26_393)

print(djia)

djia = Stock(djia.symbol, djia.year, djia.month, djia.day, djia.open, djia.high, djia.low, 10000)

print(djia)

*values, _ = djia

print(values)

print(values.append(26_393))

print(values)

djia = Stock(*values)

print(djia)

a = [1, 2, 3]

print(id(a))

a = a + [4, 5]

print(a)

print(id(a))

a = [1, 2, 3]

print(id(a))

a.append(4)

print(a)

print(id(a))

a.extend([5, 6, 7])

print(a)

print(id(a))

values = djia[:7]

print(values)

print(values + (100, ))

djia = Stock(*(values + (100, )))

print(djia)

djia = Stock(*values, 1000)

print(djia)

djia = djia._replace(year = 2019, open = 10000)

print(djia)

print(id(djia))

djia = djia._rplace(year = 2019, open = 10000)

print(djia)

print(id(djia))

djia = Stock._make(values + (100, ))

djia = djia._replace(close = 10000)

print(djia)

print(Point2D)

print(Point2D._fields)

print(Point2D._fields + ('z',))

Point3D = namedtuple('POint3D', Point2D._fields+ ('z',))

print(Point3D._fields)

print(Stock._fields)

StockExt = namedtuple('StockExt', Stock._fields + ('previous_close'))

print(StockExt._fields)

print(pt)

pt3d = Point3D(*pt, 100)

print(pt3d)

print(djia)

djia_ext = StockExt(*djia, 1_000_000)

print(djia_ext)

