class Protists:
    def __init__(self, name, weight, old):
        self.name, self.weight, self.old = name, weight, old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


m1 = Monkey("мартышка", 30.4, 7)
m2 = Monkey("шимпанзе", 24.6, 8)
p1 = Person("Балакирев", 88, 34)
p2 = Person("Верховный жрец", 67.5, 45)
f1 = Flower("Тюльпан", 0.2, 1)
f2 = Flower("Роза", 0.1, 2)
w1 = Worm("червь", 0.01, 1)
w2 = Worm("червь 2", 0.02, 1)
lst_objs = [m1, m2, p1, p2, f1, f2, w1, w2]
lst_animals = [i for i in lst_objs if isinstance(i, Animals)]
lst_plants = [i for i in lst_objs if isinstance(i, Plants)]
lst_mammals = [i for i in lst_objs if isinstance(i, Mammals)]
