class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__c = value

    def __lt__(self, other):
        if isinstance(other, Dimensions):
            left = self.a * self.b * self.c
            right = other.a * other.b * other.c
            return left < right

    def __le__(self, other):
        if isinstance(other, Dimensions):
            left = self.a * self.b * self.c
            right = other.a * other.b * other.c
            return left <= right


class ShopItem:
    def __init__(self, name, price, dim_obj):
        self.name = name
        self.price = price
        self.dim = dim_obj


shop_list = [['кеды', 1024, (40, 30, 120)],
             ['зонт', 500.24, (10, 20, 50)],
             ['холодильник', 40000, (2000, 600, 500)],
             ['табуретка', 2000.99, (500, 200, 200)]]

lst_shop = [ShopItem(i[0], i[1], Dimensions(i[2][0], i[2][1], i[2][2])) for i in shop_list]
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
