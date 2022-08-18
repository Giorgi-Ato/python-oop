class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_width', '_height') and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        object.__setattr__(self, key, value)

    def __pt_in_rect(self, x, y):
        return self._x <= x <= self._x + self._width and self._y <= y <= self._y + self._height

    def is_collision(self, rect):
        if self.__pt_in_rect(rect._x, rect._y) or self.__pt_in_rect(rect._x, rect._y + rect._height) or \
                self.__pt_in_rect(rect._x + rect._width, rect._y) or \
                self.__pt_in_rect(rect._x + rect._width, rect._y + rect._height):
            raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

lst_not_collision = []
for i in lst_rect:
    check_list = []
    for j in lst_rect:
        if not i is j:
            try:
                i.is_collision(j)
            except:
                break
            else:
                check_list.append(i)
    if len(check_list) == 3:
        lst_not_collision.append(i)
