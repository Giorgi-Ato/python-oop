class Box:
    def __init__(self):
        self.lst = []

    def add_thing(self, thn_obj):
        self.lst.append(thn_obj)

    def get_things(self):
        return self.lst

    def __eq__(self, other):
        lst = []
        for i in self.lst:
            for j in other.lst:
                if i == j:
                    lst.append(True)
        return all(lst) and len(lst) == len(self.lst)

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)
