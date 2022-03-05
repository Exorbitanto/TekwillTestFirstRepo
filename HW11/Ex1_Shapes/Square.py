from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, width):
        length = width
        super().__init__(width, length)
        # self._width = width
        # self._length = length

