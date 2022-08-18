class RenderDigit:

    def __call__(self, val, *args, **kwargs):
        try:
            return int(val)
        except:
            return None


class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.__render = render

    def __call__(self, func, *args, **kwargs):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))
        return wrapper

render = RenderDigit()

input_dg = InputValues(render)(input)
res = input_dg()
print(res)
