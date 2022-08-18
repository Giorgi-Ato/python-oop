class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []
        self._weight = 0

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing):
        if self._weight + thing.weight <= self.max_weight:
            self.__things.append(thing)
            self._weight += thing.weight

    def remove_thing(self, indx):
        self._weight -= self.__things.pop(indx)

    def get_total_weight(self):
        return self._weight
