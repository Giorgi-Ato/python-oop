class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        depth = self.depth + other.depth
        return Box3D(width, height, depth)

    def __mul__(self, other):
        width = self.width * other
        height = self.height * other
        depth = self.depth * other
        return Box3D(width, height, depth)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        width = abs(self.width - other.width)
        height = abs(self.height - other.height)
        depth = abs(self.depth - other.depth)
        return Box3D(width, height, depth)

    def __floordiv__(self, other):
        width = self.width // other
        height = self.height // other
        depth = self.depth // other
        return Box3D(width, height, depth)

    def __mod__(self, other):
        width = self.width % other
        height = self.height % other
        depth = self.depth % other
        return Box3D(width, height, depth)
