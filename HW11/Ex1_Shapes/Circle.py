from Shape import Shape

class Circle(Shape):

    def __init__(self, inner_color=None, border_color=None, radius=1):
        self.__init__(inner_color, border_color)
        self._radius = radius

    def set_radius(self, radius):
        self._raduis = radius

    def get_radius(self):
        return self._radius