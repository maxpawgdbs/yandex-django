import http

import django.db
import django.http
import django.shortcuts

import catalog.models


def home(request):
    items = (
        catalog.models.Item.objects.filter(is_on_main=True, is_published=True, category__is_published=True)
        .select_related("category", "main_image")
        .prefetch_related(
            django.db.models.Prefetch(
                "tags",
                queryset=catalog.models.Tag.objects.filter(
                    is_published=True,
                ).only("name"),
            ),
        )
        .only("id", "name", "text", "category__name", "main_image__image")
    )
    context = {
        "items": items,
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
