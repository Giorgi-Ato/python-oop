from abc import ABC, abstractmethod


# здесь объявляйте классы

class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, val):
        self._population = val

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, val):
        self._square = val

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"
