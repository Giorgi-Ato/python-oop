import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot = {'Mechanical': None, 'Aragon': None, 'Calcium': None}

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and type(filter) == Mechanical:
            self.slot['Mechanical'] = filter

        if slot_num == 2 and type(filter) == Aragon:
            self.slot['Aragon'] = filter

        if slot_num == 3 and type(filter) == Calcium:
            self.slot['Calcium'] = filter

    def remove_filter(self, slot_num):
        dct = {1: 'Mechanical', 2: 'Aragon', 3: 'Calcium'}
        self.slot[dct[slot_num]] = None

    def get_filters(self):
        return tuple(self.slot.values())

    def water_on(self):
        if all([value != None for value in self.slot.values()]) and \
                all([time.time() - i.date <= self.MAX_DATE_FILTER for i in self.slot.values()]):
            return True
        return False


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)

