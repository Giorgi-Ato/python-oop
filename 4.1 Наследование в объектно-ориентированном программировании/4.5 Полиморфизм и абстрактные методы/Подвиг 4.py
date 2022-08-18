class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):

    def __init__(self, name, weight, price):
        self._name, self._weight, self._price = name, weight, price
        self.__id = hash(self)

    def __hash__(self):
        return hash((self._name, self._weight, self._price))

    def get_id(self):
        return self.__id
