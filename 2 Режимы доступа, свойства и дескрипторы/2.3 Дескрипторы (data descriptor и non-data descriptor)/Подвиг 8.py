class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def __check_price(self, price):
        if type(price) == int and 0 <= price <= self.max_value:
            return True

    def __set_name__(self, owner, name):
        self.name = '-' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_price(value):
            setattr(instance, self.name, value)


class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length, self.max_length = min_length, max_length

    def __check_str(self, sting):
        if type(sting) == str and self.min_length <= len(sting) <= self.max_length:
            return True

    def __set_name__(self, owner, name):
        self.name = '-' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_str(value):
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)
