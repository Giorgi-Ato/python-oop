from string import ascii_letters, digits
from random import randint, choice


class EmailValidator:
    CHEK_SYMBOL = ascii_letters + digits + '_' + '.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email) == False:
            return False
        if set(email) > set(cls.CHEK_SYMBOL):
            return False
        if email.count('@') > 1:
            return False
        if len(email[:email.index('@')]) > 100:
            return False
        if len(email[email.index('@'):]) > 50:
            return False
        if email[email.index('@'):].count('.') < 1:
            return False
        for i in range(len(email)):
            if email[i] == '.' and email[i + 1] == '.':
                return False
        return True

    @classmethod
    def get_random_email(cls):
        email = ''
        end = '@gmail.com'
        for i in range(randint(1, 100)):
            email += choice(cls.CHEK_SYMBOL)
        return email + end

    @staticmethod
    def __is_email_str(email):
        if isinstance(email, str):
            return True
        return False

    @classmethod
    def __del__(cls):
        cls.obj = None


em = EmailValidator()
em2 = EmailValidator()
