class Car:

    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, name):
        if isinstance(name, str) and len(name) in range(*[2, 100]):
            self.__model = name
