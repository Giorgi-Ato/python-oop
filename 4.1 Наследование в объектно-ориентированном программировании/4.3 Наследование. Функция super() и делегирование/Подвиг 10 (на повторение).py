class ItemAttrs:
    def __init__(self, x, y):
        self.coords = [x, y]

    def __getitem__(self, item):
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value


class Point(ItemAttrs):
    pass
