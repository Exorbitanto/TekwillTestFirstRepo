from Circle import Circle
from Rectangle import Rectangle
from Square import Square

Circle1 = Circle("red", "blue", 5)
Circle2 = Circle("magenta", "olive", 4)
Circle3 = Circle("brown", "khaki", 18)

print(Circle1 + Circle3)

Rectangle1 = Rectangle("red", "blue", 5, 4 )
Rectangle2 = Rectangle("magenta", "olive", 10, 12)
Rectangle3 = Rectangle("brown", "khaki", 25, 48)

print(Rectangle1 + Rectangle3)

Square1 = Square("red", "blue", 4,4)
Square2 = Square("brown", "khaki", 25,25)
print(Square1 + Square2)

print(Rectangle3 + Square1)