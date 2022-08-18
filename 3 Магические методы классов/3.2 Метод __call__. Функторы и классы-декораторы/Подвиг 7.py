class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, request, *args, **kwargs):
        return self.get(self.__fn, request)

    def get(self, func, request, *args, **kwargs):
        if request.get('method', 'GET') == 'GET':
            return f"GET: {func(request)}"
        return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)
