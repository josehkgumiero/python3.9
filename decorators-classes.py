from fractions import Fraction

f = Fraction(2, 3)

print(
    f.denominator
)

print(
    f.numerator
)

Fraction.speak = 100

print(
    f.speak
)

Fraction.speak = lambda self, message: "Fraction says: {0}".format(message)

print(
    f.speak("This is a late parrot")
)

f2 = Fraction(10, 5)

print(
    f2.speak("This parrot is no more")
)

Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(2, 3)

f2 = Fraction(64, 8)

print(
    f1
)

print(
    f2
)

print(
    f1.is_integral()
)

print(
    f2.is_integral()
)

def dec_speak(cls):
    cls.speak = lambda self, message: "{0} says: {1}".format(self.__class__.__name__,message)
    return cls

Fraction = dec_speak(Fraction)

f1 = Fraction(2, 3)

print(
    f1.speak("Hello")
)

class Person:
    pass

Person = dec_speak(Person)

p = Person()

print(
    p.speak("This works!")
)

from datetime import datetime, timezone

def info(self):
    results = []
    results.append("time: {0}".format(datetime.now(timezone.utc)))
    results.append("Class: {0}".format(self.__class__.__name__))
    results.append("Id: {0}".format(hex(id(self))))
    for k, v in vars(self).items():
        results.append("{0}: {1}".format(k, v))
    return results

def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def say_hi():
        return "Hello There!"

p = Person('John', 1939)

print(
    p.debug()
)

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.ake = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError("Speed can not exceed top_speed")
        else:
            self._speed = new_speed

favorite = Automobile("Ford", "Model T", 1908, 45)

print(
    favorite.debug()
)

favorite.speed = 40

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0,0)

print(
    abs(p1)
)

print(
    p1 is p2
)

print(
    p2 is p3
)

print(
    p1 == p2
)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x== other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented
    
    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __ne__(self, other):
        pass

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

print(
    p1 == p2
)

print(
    p3 < p1
)

p4 = Point(100, 100)

print(
    p4 < p1
)

print(
    p4 > p1
)

from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x== other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)

print(
    p4 > p1
)

print(
    p2 <= p3
)

