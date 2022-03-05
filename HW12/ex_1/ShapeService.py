class ShapeService:

    @staticmethod
    def create_default_circle(radius=1, inner_color="white", border_color="black"):
        from Circle import Circle
        return Circle(inner_color, border_color, radius)

    @staticmethod
    def create_default_rectangle(length=1, width=1, inner_color="white", border_color="black"):
        from Rectangle import Rectangle
        return Rectangle(inner_color, border_color, length, width)

    @staticmethod
    def create_default_square(side_length, inner_color="white", border_color="black"):
        length = side_length
        width = side_length
        from Square import Square
        return Square(inner_color, border_color, length, width)

    @staticmethod
    def color_shapes(list_of_shapes, new_inner_color, new_border_color):
        for shape in list_of_shapes:
            shape.inner_color = new_inner_color
            shape.border_color = new_border_color
        return list_of_shapes