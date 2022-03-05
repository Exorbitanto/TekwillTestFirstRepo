from Rectangle import Rectangle
from my_library.numeric_tools import verify_if_value_is_positive


class Square(Rectangle):

    @property
    def area(self):
        return self.width * self.length

    def __init__(self, inner_color=None, border_color=None, length=1, width=1):
        super().__init__(inner_color, border_color)
        if verify_if_value_is_positive(length) and verify_if_value_is_positive(width):
            self._length = length
            self._width = width

    def __eq__(self, other):
        return super().__eq__(other)

    def __str__(self):
        return f"{self.inner_color} and {self.border_color} square with the lenth of {self.length} the width of {self.width} and the area of {self.area}"

    def __add__(self, other):
        return super().__mul__(other)

    def __sub__(self, other):
        return super().__sub__(other)

    def __mul__(self, other):
        return super().__mul__(other)



