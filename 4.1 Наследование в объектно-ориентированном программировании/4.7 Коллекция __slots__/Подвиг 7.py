class Note:

    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si', '_notes'

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self._do = Note('до')
        self._re = Note('ре')
        self._mi = Note('ми')
        self._fa = Note('фа')
        self._solt = Note('соль')
        self._la = Note('ля')
        self._si = Note('си')
        self._notes = [self._do, self._re, self._mi, self._fa, self._solt, self._la, self._si]

    def __check(self, val):
        if val < 0 or val > 6:
            raise IndexError('недопустимый индекс')

    def __getitem__(self, item):
        self.__check(item)
        return self._notes[item]

    def __setitem__(self, key, value):
        self.__check(key)
        self._notes[key]._ton = value
