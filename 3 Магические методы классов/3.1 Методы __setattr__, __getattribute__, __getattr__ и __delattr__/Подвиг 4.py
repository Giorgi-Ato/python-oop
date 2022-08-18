class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []


    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = id(self)


    def __setattr__(self, key, value):
        if key == 'name' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('weight','price') and (type(value) not in (int, float) or value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'id' and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)
