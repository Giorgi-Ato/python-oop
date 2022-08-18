class SellItem:
    def __init__(self, name, price):
        self.name, self.price = name, price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        self.name = name
        self.obj_ls = []

    def add_object(self, obj):
        self.obj_ls.append(obj)

    def remove_object(self, obj):
        if obj in self.obj_ls:
            self.obj_ls.pop(obj)

    def get_objects(self):
        return self.obj_ls
