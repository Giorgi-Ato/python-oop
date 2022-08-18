class Aircraft:

    def __init__(self, model, mass, speed, top):
        self._model, self._mass, self._speed, self._top = model, mass, speed, top

    def __verify_model(self, val):
        if not isinstance(val, str):
            raise TypeError('неверный тип аргумента')

    def __verify(self, val):
        if not val > 0:
            raise TypeError('неверный тип аргумента')

    def __setattr__(self, key, value):
        if key == "_model":
            self.__verify_model(value)
        elif key in ("_mass", "_speed", "_top"):
            self.__verify(value)
        elif key == "_chairs":
            if not isinstance(value, int) or not value > 0:
                raise TypeError('неверный тип аргумента')
        elif key == "_weapons":
            if not isinstance(value, dict):
                raise TypeError('неверный тип аргумента')
        object.__setattr__(self, key, value)


class PassengerAircraft(Aircraft):

    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

air = Aircraft('МС-21', 1250, 8000, 12000.5)
print(air.__dict__)
