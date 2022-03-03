from Shape import Shape

class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def set_radius(self, radius):
        self._raduis = radius

    def get_radius(self):
        return self._radius