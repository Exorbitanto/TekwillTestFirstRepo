from Square import Square
from Rectangle import Rectangle

new_square = Square(6)

print(new_square.get_length())
print(new_square.get_width())

new_square.set_inner_color("blue")
print(new_square.get_inner_color())

new_square.set_border_color("Magenta")
print(new_square.get_border_color())

new_rectangle = Rectangle(14,22,"Blue","Red")
print(new_rectangle.get_length())
print(new_rectangle.get_width())
print(new_rectangle.get_inner_color())
print(new_rectangle.get_border_color())