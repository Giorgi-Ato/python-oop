class Vector:
    CLASS_TYPE = (int, float)

    def __init__(self, *args):
        self.__check_type(args)
        self.coords = args

    def __check_type(self, value):
        if not all(type(x) in self.CLASS_TYPE for x in value):
            raise ValueError('координаты должны быть целыми числами')

    def __check_len(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return self.coords

    def __make_vector(self, *coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.__check_len(other)
        crds = [i[0] + i[1] for i in list(zip(self.coords, other.coords))]
        return self.__make_vector(*crds)

    def __sub__(self, other):
        self.__check_len(other)
        crds = [i[0] - i[1] for i in list(zip(self.coords, other.coords))]
        return self.__make_vector(*crds)


class VectorInt(Vector):
    CLASS_TYPE = int,
