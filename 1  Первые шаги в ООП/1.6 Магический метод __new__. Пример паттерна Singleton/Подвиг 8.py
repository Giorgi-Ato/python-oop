TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        ibj = None
        if TYPE_OS == 1:
            ibj = super().__new__(DialogWindows)
        else:
            ibj = super().__new__(DialogLinux)
        ibj.name = args[0]
        return ibj

    def __init__(self, name):
        self.name = name
