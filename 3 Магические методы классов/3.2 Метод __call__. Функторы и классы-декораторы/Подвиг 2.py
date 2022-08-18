from random import randint, choice


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_lenght = min_length
        self.max_lenght = max_length

    def __call__(self):
        psw_length = randint(self.min_lenght, self.max_lenght)
        return ''.join([choice(self.psw_chars) for _ in range(psw_length)])

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
psw = rnd()
lst_pass = [rnd() for i in range(3)]
print(lst_pass)
