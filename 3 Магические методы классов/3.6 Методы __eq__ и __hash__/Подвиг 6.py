import sys


# здесь объявляйте классы
class ShopItem:
    def __init__(self, name, weight, price):
        self.name, self.weight, self.price = name, weight, price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!
new_lst = [ShopItem(i.split(':')[0], i.split(':')[1].split()[0], i.split(':')[1].split()[1]) for i in lst_in]

shop_items = {i: (i, new_lst.count(i)) for i in new_lst}
