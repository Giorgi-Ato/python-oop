class Thing:
    ID = 0

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        Thing.ID += 1
        self.id = Thing.ID
        self.name, self.price, self.weight, self.dims, self.memory, self.frm = name, price, weight, dims, memory, frm

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm


class Table(Thing):

    def __init__(self, name, price, weight=None, dims=None):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):

    def __init__(self, name, price, memory=None, frm=None):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
