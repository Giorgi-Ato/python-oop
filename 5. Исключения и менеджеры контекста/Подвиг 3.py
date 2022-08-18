class ValidatorString:

    def __init__(self, min_length, max_length, chars):
        self.__min_length = min_length
        self.__max_length = max_length
        self.__chars = chars

    def is_valid(self, string):
        if not self.__min_length <= len(string) <= self.__max_length or \
                self.__chars and not any(char in self.__chars for char in string):
            raise ValueError('недопустимая строка')
        return string


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = self._password = None

    def form(self, request):
        if not request.get('login') or not request.get('password'):
            raise TypeError('в запросе отсутствует логин или пароль')

        self._login = self.login_validator.is_valid(request.get('login'))
        self._password = self.password_validator.is_valid(request.get('password'))
