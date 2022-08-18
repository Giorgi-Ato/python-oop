class Tuple(tuple):
    def __add__(self, other):
        if type(other) != tuple:
            return Tuple((list(self) + list(other)))
        else:
            super().__add__(other)
