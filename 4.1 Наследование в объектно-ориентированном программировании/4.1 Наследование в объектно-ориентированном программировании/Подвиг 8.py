class Validator:

    def __call__(self, *args, **kwargs):
        for i in list(args):
            if not self._is_valid(i):
                raise ValueError('данные не прошли валидацию')

    def _is_valid(self, data):
        return True


class IntegerValidator(Validator):
    CLASS_VALIDATOR = int

    def __init__(self, min_value, max_value):
        self.min_value, self.max_value = min_value, max_value

    def _is_valid(self, data):
        if not type(data) == self.CLASS_VALIDATOR or not (self.min_value <= data <= self.max_value):
            return False
        return True


class FloatValidator(Validator):
    CLASS_VALIDATOR = float

    def __init__(self, min_value, max_value):
        self.min_value, self.max_value = min_value, max_value

    def _is_valid(self, data):
        if not type(data) == self.CLASS_VALIDATOR or not (self.min_value <= data <= self.max_value):
            return False
        return True
