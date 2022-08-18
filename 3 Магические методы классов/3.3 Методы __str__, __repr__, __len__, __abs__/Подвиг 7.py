class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = [0 for i in range(args[0])]
        else:
            self.coords = list(args)

    def set_coords(self, *args):
        for i in range(len(args)):
            self.coords[i] = args[i]

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sum([i ** 2 for i in self.coords]) ** 0.5
