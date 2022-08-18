class FloatValue:
    def verify_value(self, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, val):
        self.value = val


class TableSheet:

    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for _ in range(m)] for __ in range(n)]


table = TableSheet(5, 3)
val = 1.0
for i in table.cells:
    for j in i:
        j.value = val
        val += 1
