class Shape:

    def __init__(self, inner_color=None, border_color=None):
        self._inner_color = inner_color
        self._border_color = border_color

    def get_inner_color(self):
        return self._inner_color

    def get_border_color(self):
        return self._border_color

    def set_inner_color(self, inner_color):
        self._inner_color = inner_color

    def set_border_color(self, border_color):
        self._border_color = border_color
