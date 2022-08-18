class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        if isinstance(other, (int, float)):
            return self.money + other

    def __radd__(self, other):
        return self + other


class Budget:
    def __init__(self):
        self.ls = []

    def add_item(self, it_obj):
        self.ls.append(it_obj)

    def remove_item(self, indx):
        self.ls.pop(indx)

    def get_items(self):
        return self.ls
