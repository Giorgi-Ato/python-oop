class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, val):
        self.__kind = val

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, val):
        self.__old = val

s = """Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3"""

animals = [Animal(*line.split('; ')) for line in s.splitlines()]
