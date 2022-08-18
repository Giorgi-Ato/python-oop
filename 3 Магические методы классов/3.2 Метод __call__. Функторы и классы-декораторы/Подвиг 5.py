class DigitRetrieve:
    def __call__(self, string: str, *args, **kwargs):
        if string[0] == '-':
            if string[1:].isdigit():
                return -(int(string[1:]))
        elif string.isdigit():
            return int(string)
        return None

st = ["123", "abc", "-56.4", "0", "-5"]
dg = DigitRetrieve()
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
