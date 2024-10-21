from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template = "homepage/main.html"
    context = {}
    return render(request, template, context)


def teapot(request):
    return HttpResponse("Я чайник", status=HTTPStatus.IM_A_TEAPOT)


__all__ = [
    home,
    teapot,
]
