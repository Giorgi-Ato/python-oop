class Triangle:
    def __init__(self, a, b, c):
        if a < b + c or b < a + c or c < a + b:
            self.a, self.b, self.c = a, b, c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return self.a + self.b + self.c

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        self.__c = value
