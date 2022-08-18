class AppStore:
    apps = []

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        self.apps.remove(app)

    def block_application(self, app):
        app.blocked = False

    def total_apps(self):
        return len(self.apps)


class Application:

    def __init__(self, name):
        self.name = name
        self.blocked = True

store = AppStore()
app_youtube = Application("Youtube")
print(app_youtube.name, app_youtube.blocked)
store.add_application(app_youtube)
print(store.apps[0].__dict__)
store.remove_application(app_youtube)
print(store.apps)
