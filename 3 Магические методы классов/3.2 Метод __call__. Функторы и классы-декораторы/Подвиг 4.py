class LengthValidator:
    def __init__(self, min_length, max_length):
        self.max_length = max_length
        self.min_length = min_length

    def __call__(self, *args, **kwargs):
        if self.min_length <= len(args[0]) <= self.max_length:
            return True
        return False


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        if set(args[0]) in set(self.chars):
            return True
        return False
