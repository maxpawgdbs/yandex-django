__all__ = ()
import re

from django.conf import settings


class MyMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def reverse_russian_words(self, m):
        return f"{m.group(0)[::-1]}"

    def __call__(self, request):
        response = self.get_response(request)
        if settings.ALLOW_REVERSE:
            MyMiddleware.count += 1
            if MyMiddleware.count == 10:
                MyMiddleware.count = 0
                decode = response.content.decode("utf8")
                response.content = re.sub(
                    r"\b[а-яА-ЯёЁ]+\b",
                    self.reverse_russian_words,
                    decode,
                ).encode("utf8")

        return response
