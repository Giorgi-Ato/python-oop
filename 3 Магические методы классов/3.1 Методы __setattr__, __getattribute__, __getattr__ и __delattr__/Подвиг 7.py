class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []
        self.types = []

    def add_app(self, app_obj):
        if type(app_obj) not in self.types:
            self.apps.append(app_obj)
            self.types.append(type(app_obj))

    def remove_app(self, app_obj):
        if app_obj in self.apps:
            self.apps.remove(app_obj)

class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"

class AppYouTube:
    def __init__(self, memory_max):
        self.memory_max = memory_max
        self.name = "YouTube"

class AppPhone:
    def __init__(self, dct):
        self.name = "Phone"
        self.phone_list = dct
