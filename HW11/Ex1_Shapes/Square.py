from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, width, length):

        if width != length:
            raise Exception("The length and width of the square should be the same, please try again.")
        super().__init__(width, length)
        # self._width = width
        # self._length = length
