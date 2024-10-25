import http

import django.http
import django.shortcuts


def home(request):
    template = "homepage/main.html"
    return django.shortcuts.render(request, template)


def teapot(request):
    return django.http.HttpResponse(
        "Я чайник",
        status=http.HTTPStatus.IM_A_TEAPOT,
    )


__all__ = (
    home,
    teapot,
)
