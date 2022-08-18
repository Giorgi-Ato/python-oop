class Viber:
    msg = []

    @classmethod
    def add_message(cls, msg):
        cls.msg.append(msg)

    @classmethod
    def remove_message(cls, msg):
        if msg in cls.msg:
            cls.msg.remove(msg)

    @staticmethod
    def set_like(msg):
        if msg.fl_like == False:
            msg.fl_like = True
        else:
            msg.fl_like = False

    def show_last_message(self, number):
        num = len(self.msg) - number
        print(self.msg[num:])

    @classmethod
    def total_messages(cls):
        return len(cls.msg)


class Message:

    def __init__(self, text):
        self.text = text
        self.fl_like = False
