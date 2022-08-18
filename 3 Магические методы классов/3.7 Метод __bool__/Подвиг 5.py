import sys


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from, self.title, self.content, self.is_read = mail_from, title, content, False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list = [MailItem(i.split(';')[0], i.split(';')[1], i.split(';')[2]) for i in lst_in]


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(lambda x: bool(x) == True, mail.inbox_list))
