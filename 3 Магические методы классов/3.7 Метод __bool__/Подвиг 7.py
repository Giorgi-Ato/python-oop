class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args
        self.ar = len(args)

    def __bool__(self):
        return self.ar == 4

    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8), Ellipse(), Ellipse()]

[i.get_coords() for i in lst_geom if i]
