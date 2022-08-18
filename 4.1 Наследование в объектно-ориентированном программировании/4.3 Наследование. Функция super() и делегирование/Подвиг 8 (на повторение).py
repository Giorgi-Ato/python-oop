class SoftList(list):

    def __getitem__(self, item):
        if not (-len(self) <= item < len(self)):
            return False
        return  super().__getitem__(item)
