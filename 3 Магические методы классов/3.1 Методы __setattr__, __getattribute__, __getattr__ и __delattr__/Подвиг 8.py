class Circle:

    def __init__(self, x, y, radius):
        self.__x = self.__y = self.__radius = 0
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) in (int, float):
            self.__x = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) in (int, float):
            self.__y = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif value <= 0:
            return
        self.__radius = value

    def __getattr__(self, item):
        return False
