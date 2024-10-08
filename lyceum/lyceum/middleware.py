import re

from django.conf import settings


def n():
    if not hasattr(n, "counter"):
        n.counter = 0
    n.counter += 1
    if n.counter == 10:
        n.counter = 0
        return True
    else:
        return False


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.ALLOW_REVERSE:
            if n():
                response.content = re.sub(
                    r"\w+[а-яА-ЯёЁ]",
                    lambda m: f"{m.group(0)[::-1]}",
                    response.content.decode("utf8"),
                ).encode("utf8")
        return response
