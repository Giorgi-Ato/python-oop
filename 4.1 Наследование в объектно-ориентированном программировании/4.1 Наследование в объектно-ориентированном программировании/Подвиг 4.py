class Animal:
    def __init__(self, name, old):
        self.name, self.old = name, old


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color, self.weight = color, weight


    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"

class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed, self.size = breed, size

    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"
