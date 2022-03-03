from Shape import Shape


class Rectangle(Shape):

    def __init__(self, width=1, length=1):
        self._width = width
        self._length = length

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def set_length(self, length):
        self._length = length

    def set_width(self, width=1):
        self._width = width
