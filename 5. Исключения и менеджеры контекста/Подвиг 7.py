# здесь объявляйте класс
class TupleLimit(tuple):
    def __new__(cls, lst, max_length, **kwargs):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __str__(self):
        return ' '.join(str(float(i)) for i in self)

    def __repr__(self):
        return ' '.join(str(float(i)) for i in self)



digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

# здесь создавайте объект класса
try:
    tl = TupleLimit(digits, 5)
except ValueError as e:
    print(e)
else:
    print(tl)
