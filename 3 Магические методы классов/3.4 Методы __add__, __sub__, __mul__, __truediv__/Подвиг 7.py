class Book:
    def __init__(self, title, author, year):
        self.title, self.author, self.year = title, author, year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
        return self

    def __iadd__(self, other):
        self + other
        return self

    def __sub__(self, other):
        if isinstance(other, (Book, int)):
            if type(other) == Book and other in self.book_list:
                self.book_list.remove(other)
            else:
                self.book_list.pop(other)
        return self

    def __isub__(self, other):
        self - other
        return self

    def __len__(self):
        return len(self.book_list)
