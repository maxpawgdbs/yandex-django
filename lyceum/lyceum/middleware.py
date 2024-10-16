import re

from django.conf import settings


class MyMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.ALLOW_REVERSE:
            MyMiddleware.count += 1
            if MyMiddleware.count == 10:
                MyMiddleware.count = 0
                response.content = re.sub(
                    r"\w+[а-яА-ЯёЁ]",
                    lambda m: f"{m.group(0)[::-1]}",
                    response.content.decode("utf8"),
                ).encode("utf8")
        return response
