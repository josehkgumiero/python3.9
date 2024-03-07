class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def to_string(self):
        return \
            '''Rectangle: _width={0}, _height={1}''' \
            .format(self._width, self._height)
    
    def __str__(self):
        return \
            '''Rectangle: _width={0}, _height={1}''' \
            .format(self._width, self._height)
    
    def __repr__(self):
        return \
            '''Rectangle({0}, {1})''' \
            .format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return \
                self._width == other._width \
                and self._height == other._height
        else:
            return \
                False

    @property
    def width(self):
        return \
            self._width
    
    @width.setter
    def width(self, width):
        if \
            width <= 0:
                raise \
                    ValueError('''Width must be positive.''')
        else:
            self._width = width
    
    @property
    def height(self):
        return \
            self._height

    @height.setter
    def width(self, height):
        if \
            height <= 0:
                raise \
                    ValueError('''Height must be positive.''')
        else:
            self._height = height

r_1 = Rectangle(10 ,20)

print(
    r_1._width
)

r_1._width = 100

print(
    r_1._width
)

r_2 = Rectangle(10 , 20)

print(
    r_2.area()
)

print(
    r_2.perimeter()
)

print(
    r_2
)

print(
    hex(id(r_2))
)