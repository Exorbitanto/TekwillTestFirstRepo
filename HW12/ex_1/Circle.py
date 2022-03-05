from my_library.numeric_tools import verify_if_value_is_positive
from Shape import Shape
import math


class Circle(Shape):

    def __init__(self, inner_color=None, border_color=None, radius=1):
        super().__init__(inner_color, border_color)
        if verify_if_value_is_positive(radius):
            self._radius = radius

    def __str__(self):
        return f"{self.inner_color} and {self.border_color} circle with the radius of {self.radius}"

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise Exception("You cannot compare objects from different classes.")
        elif self._radius == other.radius and self.border_color == other.border_color and self.inner_color == other.inner_color:
            return True
        else:
            return False

    def __add__(self, other):
        if not isinstance(other, Circle):
            raise Exception("You cannot add objects from different classes.")
        return Circle(self.inner_color, self.border_color, self.radius + other.radius)

    def __sub__(self, other):
        if not isinstance(other, Circle):
            raise Exception("You cannot subtract objects from different classes.")
        if self.radius < other.radius:
            raise Exception("You cannot subtract a bigger object from a lesser one.")
        return Circle(self.inner_color, self.border_color, self.radius - other.radius)

    def __mul__(self, other):
        if not isinstance(other, Circle) and type(other) != int and type(other) != float:
            raise Exception("The multiplier should be a number of another object of the same type.")
        if type(other) != int or type(other) != float:
            return Circle(self.inner_color, self.border_color, self.radius * other)
        else:
            return Circle(self.inner_color, self.border_color, self.radius * other.radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if verify_if_value_is_positive(radius):
            self._radius = radius

    @property
    def area(self):
        return self._radius ** 2 * math.pi


