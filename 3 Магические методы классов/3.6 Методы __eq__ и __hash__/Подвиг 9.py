class Dimensions:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __setattr__(self, key, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


def mp(txt: str):
    txt = list(map(float, txt.split()))
    return txt

s_inp = list(map(mp, input().split(';')))  # эту строку (переменную s_inp) в программе не менять

lst_dims = sorted([Dimensions(i[0], i[1], i[2]) for i in s_inp], key=lambda x: hash(x))
