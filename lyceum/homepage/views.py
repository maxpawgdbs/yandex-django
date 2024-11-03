import http

import django.db
import django.http
import django.shortcuts

import catalog.models
import homepage.forms


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
    if request.method == "GET":
        template = "homepage/echo.html"
        return django.shortcuts.render(request, template)

    return django.http.HttpResponseNotAllowed(
        "Страничка доступна только по GET-запросу)",
    )


def echo_submit(request):
    if request.method == "POST":
        form = homepage.forms.EchoForm(request.POST)
        text = form.cleaned_data["text"]
        if form.is_valid():
            return django.http.HttpResponse(text)

    return django.http.HttpResponseNotAllowed(
        "Страничка доступна только по POST-запросу)",
    )


__all__ = ()
