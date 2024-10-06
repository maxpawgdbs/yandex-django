import re

from django.conf import settings

n = 0


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        global n
        n += 1
        if n == 10:
            n = 0
            if settings.ALLOW_REVERSE:
                response.content = re.sub(
                    r"\w+[а-яА-ЯёЁ]",
                    lambda m: f"{m.group(0)[::-1]}",
                    response.content.decode("utf8"),
                ).encode("utf8")
        return response
