class Digit:
    def __init__(self, val):
        if not isinstance(val, (float, int)):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, val):
        super().__init__(val)
        if not isinstance(val, int):
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, val):
        super().__init__(val)
        if not isinstance(val, float):
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):

    def __init__(self, val):
        super().__init__(val)
        if not val > 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):

    def __init__(self, val):
        super().__init__(val)
        if not val < 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(1), PrimeNumber(2), PrimeNumber(3),
          FloatPositive(1.1), FloatPositive(2.2),
          FloatPositive(3.3), FloatPositive(4.4),
          FloatPositive(5.5)
          ]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
