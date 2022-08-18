class StringDigit(str):
    def __init__(self, val: str):
        if not val.isdigit():
            raise ValueError("в строке должны быть только цифры")
        str.__init__(val)

    def __add__(self, other):
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        return StringDigit(StringDigit(other) + self)
