class Track:
    def __init__(self, start_x, start_y):
        self.start_x, self.start_y = start_x, start_y
        self.point = []

    def add_point(self, x, y, speed):
        self.point.append([x, y, speed])

    def __check_value(self, value):
        if not isinstance(value, int) or value < 0:
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.__check_value(item)

        return [(self.point[item][0], self.point[item][1]), self.point[item][2]]

    def __setitem__(self, key, value):
        self.__check_value(key)
        self.point[key][2] = value

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)
