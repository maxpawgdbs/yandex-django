import http

import django.db
import django.http
import django.shortcuts

import catalog.models


def home(request):
    context = {
        "items": catalog.models.Item.objects.on_main(),
    }
    template = "homepage/main.html"
    return django.shortcuts.render(request, template, context=context)


def teapot(request):
    return django.http.HttpResponse(
        "Я чайник",
        status=http.HTTPStatus.IM_A_TEAPOT,
    )


__all__ = (
    home,
    teapot,
)
