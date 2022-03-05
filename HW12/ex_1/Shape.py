class Shape:

    def __init__(self, inner_color=None, border_color=None):
        self._inner_color = inner_color
        self._border_color = border_color

    def __add__(self, other):
        if not isinstance(other, Shape):
            raise Exception("You cannot compare objects from different classes.")
        else:
            raise Exception("The shape has only colors as proprieties and cannot be added.")

    def __eq__(self, other):
        if not isinstance(other, Shape):
            raise Exception("You cannot compare objects from different classes.")
        elif self.border_color == other.border_color and self.inner_color == other.inner_color:
            return True
        else:
            return False

    @property
    def inner_color(self):
        return self._inner_color

    @property
    def border_color(self):
        return self._border_color

    @inner_color.setter
    def inner_color(self, inner_color):
        self._inner_color = inner_color

    @border_color.setter
    def border_color(self, border_color):
        self._border_color = border_color
