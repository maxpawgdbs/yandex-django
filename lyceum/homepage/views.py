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


def echo(request):
    template = "homepage/echo.html"
    return django.shortcuts.render(request, template)


def echo_submit(request):
    if request.method == "POST":
        return django.http.HttpResponse(str(request.POST["text"]))
    return django.http.HttpResponseForbidden("ТЫ КУДА ПОЛЕЗ")


__all__ = ()
