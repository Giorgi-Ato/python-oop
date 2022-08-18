class ListMath:
    def __init__(self, ls=[]):
        self.lst_math = [i for i in ls if type(i) in (int, float)]

    def __add__(self, other):
        return ListMath([i + other for i in self.lst_math])

    def __radd__(self, other):
        return ListMath([i + other for i in self.lst_math])

    def __iadd__(self, other):
        self.lst_math = [i + other for i in self.lst_math]
        return self

    def __sub__(self, other):
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - i for i in self.lst_math])

    def __isub__(self, other):
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __mul__(self, other):
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        return ListMath([i * other for i in self.lst_math])

    def __imul__(self, other):
        self.lst_math = [i * other for i in self.lst_math]
        return self

    def __truediv__(self, other):
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / i for i in self.lst_math])

    def __itruediv__(self, other):
        self.lst_math = ListMath([i / other for i in self.lst_math])
        return self
