from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        check = [number[4], number[9], number[14]]
        if not all(map(lambda x: x == '-', check)):
            return False
        elif not number.replace('-', '').isnumeric():
            return False
        return True

    @classmethod
    def check_name(cls, name):
        return isinstance(name, str) and len(name.split()) < 3 and set(name.replace(' ', '')) <= set(cls.CHARS_FOR_NAME)


print(CardCheck.check_card_number("12A4-5678-9012-0000"))
print((CardCheck.check_name('SERGEI BALAKIREV NAM')))
