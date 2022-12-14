class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table = {}

    def update_indx(self):
        self.rows = max(key[0] for key in self.table) + 1
        self.cols = max(key[1] for key in self.table) + 1

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.update_indx()

    def remove_data(self, row, col):
        try:
            del self.table[(row, col)]
            self.update_indx()
        except KeyError:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        try:
            return self.table[item[0], item[1]].value
        except KeyError:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        item = (key[0], key[1])
        if item not in self.table:
            self.table[item] = Cell(value)
            self.update_indx()
        else:
            self.table[item] = Cell(value)
