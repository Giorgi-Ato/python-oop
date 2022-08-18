class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.y = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)) and self.MIN_COORD <= x <= self.MAX_COORD:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)) and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2
