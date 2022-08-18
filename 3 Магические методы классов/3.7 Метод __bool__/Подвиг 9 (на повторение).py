class Vector:
    def __init__(self, *args):
        self.coords = args

    def __setattr__(self, key, value):
        if all(list(map(lambda x: isinstance(x, (int, float)), value))):
            object.__setattr__(self, key, value)

    def __add__(self, other):
        if isinstance(other, (float, int)):
            self.coords = tuple(i + other for i in self.coords)
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            vl = zip(self.coords, other.coords)
            new_vl = tuple(i[0] + i[1] for i in vl)
            return Vector(*new_vl)

    def __iadd__(self, other):
        self + other
        return self

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            self.coords = tuple(i - other for i in self.coords)
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            vl = zip(self.coords, other.coords)
            new_vl = tuple(i[0] - i[1] for i in vl)
            return Vector(*new_vl)

    def __isub__(self, other):
        self - other
        return self

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            self.coords = tuple(i * other for i in self.coords)
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            vl = zip(self.coords, other.coords)
            new_vl = tuple(i[0] * i[1] for i in vl)
            return Vector(*new_vl)

    def __imul__(self, other):
        self * other
        return self

    def __eq__(self, other):
        vl = zip(self.coords, other.coords)
        return all([i[0] == i[1] for i in vl])
