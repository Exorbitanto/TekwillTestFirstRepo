from Shape import Shape

class Rectangle(Shape):

    def __init__(self, width =1 , length =1 ):
        self.width = width
        self.length = length

    def get_lengh(self):
        return self.length

    def set_lengh(self, length):
        self.length = length