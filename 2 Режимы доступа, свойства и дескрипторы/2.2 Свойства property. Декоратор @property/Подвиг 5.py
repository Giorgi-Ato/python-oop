class WindowDlg:

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__height}, {self.__width}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if isinstance(width, int) and width in range(0, 10001):
            self.__width = width
            self.show()
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int) and height in range(0, 10001):
            self.__height = height
            self.show()
