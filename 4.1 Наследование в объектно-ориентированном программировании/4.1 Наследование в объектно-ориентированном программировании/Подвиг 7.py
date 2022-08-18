class Singleton:
    is_obj = None

    def __new__(cls, *args, **kwargs):
        if not Singleton.is_obj:
            Singleton.is_obj = super().__new__(cls)
        return Singleton.is_obj


class Game(Singleton):
    def __init__(self, name):
        if "name" not in Singleton.__dict__:
            self.name = name
