class Point:
    def __init__(self, x, y):
        self.__x, self.__y = x, y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2=0, y2=0):
        if isinstance(x1, Point) and isinstance(y1, Point):
            self.x1 = x1.get_coords()[0]
            self.y1 = x1.get_coords()[1]
            self.x2 = y1.get_coords()[0]
            self.y2 = y1.get_coords()[1]
        else:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        self.__sp = Point(self.x1, self.y1)
        self.__ep = Point(self.x2, self.y2)

    def set_coords(self, sp, ep):
        self.x1 = sp.get_coords()[0]
        self.y1 = sp.get_coords()[1]
        self.x2 = ep.get_coords()[0]
        self.y2 = ep.get_coords()[1]

    def get_coords(self):
        return Point(self.x1, self.y1), Point(self.x2, self.y2)


    def draw(self):
        return f"Прямоугольник с координатами: {(self.x1, self.y1)} {self.x2, self.y2}"


rect = Rectangle(Point(0, 0), Point(20, 34))
