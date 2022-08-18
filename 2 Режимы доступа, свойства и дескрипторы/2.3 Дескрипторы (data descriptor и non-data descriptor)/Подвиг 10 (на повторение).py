class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, it):
        self.items.append(it)

    def remove_telecast(self, indx):
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)


class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, val):
        self.__id = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, val):
        self.__duration = val
