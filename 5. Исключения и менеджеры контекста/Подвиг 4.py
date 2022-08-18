class PrimaryKeyError(Exception):

    def __init__(self, **kwargs):
        if not 'id' in kwargs and not 'pk' in kwargs:
            self.ms = "Первичный ключ должен быть целым неотрицательным числом"
        else:
            key, value = tuple(kwargs.items())[0]
            self.ms = f"Значение первичного ключа {key} = {value} недопустимо"

    def __str__(self):
        return self.ms


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
