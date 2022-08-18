class SingletonFive:
    __cnt = 0
    __link = None

    def __new__(cls, *args, **kwargs):
        if cls.__cnt < 5:
            cls.__link = super().__new__(cls)
            cls.__cnt += 1
        return cls.__link

    def __init__(self, name):
        self.name = name
