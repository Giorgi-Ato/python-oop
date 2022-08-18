class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cd = cls


class MoneyR:
    def __init__(self, volume=0):
        self.volume = volume
        self.cd = None
        self.name = 'rub'

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, bnk_obj):
        self.__cd = bnk_obj

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, vl):
        self.__volume = vl

    def get_values(self, other):
        if self.__cd == None:
            raise ValueError("Неизвестен курс валют.")
        if not isinstance(other, (MoneyR, MoneyD, MoneyE)):
            raise TypeError("Неизвестен курс валют.")

        ex1 = self.volume / self.cd.rates[self.name]
        ex2 = other.volume / other.cd.rates[other.name]
        return ex1, ex2

    def __lt__(self, other):
        x1, x2 = self.get_values(other)
        return x1 < x2

    def __eq__(self, other):
        ex1, ex2 = self.get_values(other)
        return abs(ex1 - ex2) <= 0.1

    def __ge__(self, other):
        ex1, ex2 = self.get_values(other)
        return ex1 >= ex2


class MoneyD:
    def __init__(self, volume=0):
        self.volume = volume
        self.cd = None
        self.name = 'dollar'

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, bnk_obj):
        self.__cd = bnk_obj

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, vl):
        self.__volume = vl

    def get_values(self, other):
        if self.__cd == None:
            raise ValueError("Неизвестен курс валют.")
        if not isinstance(other, (MoneyR, MoneyD, MoneyE)):
            raise TypeError("Неизвестен курс валют.")

        ex1 = self.volume / self.cd.rates[self.name]
        ex2 = other.volume / other.cd.rates[other.name]
        return ex1, ex2

    def __lt__(self, other):
        x1, x2 = self.get_values(other)
        return x1 < x2

    def __eq__(self, other):
        ex1, ex2 = self.get_values(other)
        return abs(ex1 - ex2) <= 0.1

    def __ge__(self, other):
        ex1, ex2 = self.get_values(other)
        return ex1 >= ex2


class MoneyE:
    def __init__(self, volume=0):
        self.volume = volume
        self.cd = None
        self.name = 'euro'

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, bnk_obj):
        self.__cd = bnk_obj

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, vl):
        self.__volume = vl

    def get_values(self, other):
        if self.__cd == None:
            raise ValueError("Неизвестен курс валют.")
        if not isinstance(other, (MoneyR, MoneyD, MoneyE)):
            raise TypeError("Неизвестен курс валют.")

        ex1 = self.volume / self.cd.rates[self.name]
        ex2 = other.volume / other.cd.rates[other.name]
        return ex1, ex2

    def __lt__(self, other):
        x1, x2 = self.get_values(other)
        return x1 < x2

    def __eq__(self, other):
        ex1, ex2 = self.get_values(other)
        return abs(ex1 - ex2) <= 0.1

    def __ge__(self, other):
        ex1, ex2 = self.get_values(other)
        return ex1 >= ex2

