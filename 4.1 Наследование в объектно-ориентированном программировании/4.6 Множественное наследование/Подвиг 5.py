class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:
    def __str__(self):
        a = "\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])
        return a


class ShopUserView:
    def __str__(self):
        a = "\n".join([f"{key}: {value}" for key, value in self.__dict__.items() if key != '_id'])
        return a


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year
