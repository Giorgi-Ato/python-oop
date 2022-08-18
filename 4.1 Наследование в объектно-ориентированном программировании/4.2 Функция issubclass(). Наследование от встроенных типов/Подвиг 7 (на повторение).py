class VideoItem:
    def __init__(self, title, descr, path):
        self.title, self.descr, self.path = title, descr, path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not (0 <= value <= 5) or type(value) != int:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value
