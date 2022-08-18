class WordString:
    def __init__(self, txt=''):
        self.txt = txt

    def __call__(self, *args, **kwargs):
        return self.words(args[0])

    def __len__(self):
        return len(self.txt.split())

    def words(self, indx):
        return self.txt.split()[indx]

    @property
    def string(self):
        return self.txt

    @string.setter
    def string(self, value):
        self.txt = value

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
