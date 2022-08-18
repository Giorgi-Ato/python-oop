class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module_obj):
        self.modules.append(module_obj)

    def remove_module(self, module_indx):
        self.modules.pop(module_indx)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson_obj):
        self.lessons.append(lesson_obj)

    def remove_lesson(self, obj_indx):
        self.lessons.pop(obj_indx)


class LessonItem:
    check = ('title', 'practices', 'duration')

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('practices', 'duration') and (type(value) != int or value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.check:
            pass
