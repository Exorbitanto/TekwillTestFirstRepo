from Shape import Shape
from my_library.numeric_tools import verify_if_value_is_positive


class Rectangle(Shape):

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length=1):
        if verify_if_value_is_positive(length):
            self._length = length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width=1):
        if verify_if_value_is_positive(width):
            self._width = width

    @property
    def area(self):
        return self.width * self.length

    @staticmethod
    def is_resctangle(other):
        from Square import Square
        return isinstance(other, Rectangle) or isinstance(other, Square)

    @staticmethod
    def is_a_number(other):
        return type(other) == int or type(other) == float

    def __init__(self, inner_color=None, border_color=None, length=1, width=1):
        if verify_if_value_is_positive(length) and verify_if_value_is_positive(width):
            super().__init__(inner_color, border_color)
            self._width = width
            self._length = length

    def __eq__(self, other):
        if Rectangle.is_resctangle(other):
            if self.area == other.area and self.border_color == other.border_color and self.inner_color == other.inner_color:
                return True
            else:
                return False

    def __str__(self):
        return f"{self.inner_color} and {self.border_color} rectangle with the length of {self.length} the width of {self.width} and the area of {self.area}"

    def __add__(self, other):
        if Rectangle.is_resctangle(other):
            return Rectangle(self.inner_color, self.border_color, self.length + other.length, self.width + other.width)
        else:
            raise Exception("You cannot compare objects from different classes.")


    def __sub__(self, other):
        if Rectangle.is_resctangle(other):
            if self.length < other.length or self.width < other.width:
                raise Exception("You cannot subtract a bigger object from a lesser one.")
            return Rectangle(self.inner_color, self.border_color, self.length - other.length, self.width - other.width)
        else:
            raise Exception("You cannot compare objects from different classes.")

    def __mul__(self, other):
        if not Rectangle.is_resctangle(other) and not Rectangle.is_a_number(other):
            raise Exception("The multiplier should be a number of another object of the same type.")
        if Rectangle.is_a_number(other):
            return Rectangle(self.inner_color, self.border_color, self.length * other, self.width * other)
        else:
            return Rectangle(self.inner_color, self.border_color, self.length * other.length, self.width * other.width)


