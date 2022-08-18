from abc import ABC, abstractmethod


# здесь объявляйте классы

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):

    def __init__(self, login, password):
        self._login, self._password = login, password
        self._id = hash(self)

    def __hash__(self):
        return abs(hash((self._login, self._password)))

    def get_pk(self):
        return self._id
