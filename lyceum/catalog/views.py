import django.db
import django.http
import django.shortcuts
import django.utils

import catalog.models


def item_list(request):
    template = "catalog/item_list.html"
    items = catalog.models.Item.objects.published()
    context = {
        "items": items,
    }
    return django.shortcuts.render(request, template, context)


def item_detail(request, index):
    template = "catalog/item.html"
    items = catalog.models.Item.objects.filter(is_published=True)
    item = django.shortcuts.get_object_or_404(
        items.select_related("category", "main_image")
        .prefetch_related(
            django.db.models.Prefetch(
                "tags",
                queryset=catalog.models.Tag.objects.filter(
                    is_published=True,
                ).only("name"),
            ),
            django.db.models.Prefetch(
                "images",
                queryset=catalog.models.ItemGalery.objects.only("images"),
            ),
        )
        .only("name", "text", "category__name"),
        pk=index,
    )
    context = {
        "item": item,
    }
    return django.shortcuts.render(request, template, context)


def item_detail_re(request, index):
    return django.http.HttpResponse("<body>" + index + "</body>")


def converter(request, index):
    return django.http.HttpResponse("<body>" + str(index) + "</body>")


def unverified(request):
    template = "catalog/item_list.html"
    items = catalog.models.Item.objects.published()
    items = items.filter(created_at=django.db.models.F("updated_at"))
    context = {
        "items": items,
    }
    return django.shortcuts.render(request, template, context)


def friday(request):
    template = "catalog/item_list.html"
    items = catalog.models.Item.objects.published()
    items = items.filter(updated_at__week_day=6).order_by("updated_at")[:5]
    context = {
        "items": items,
    }
    return django.shortcuts.render(request, template, context)


def new(request):
    template = "catalog/item_list.html"
    items = catalog.models.Item.objects.published()
    items = items.filter(
        created_at__gte=django.utils.timezone.now()
        - django.utils.timezone.timedelta(hours=168),
    ).order_by("?")[:5]
    context = {
        "items": items,
    }
    return django.shortcuts.render(request, template, context)


__all__ = (
    item_detail,
    item_detail_re,
    item_list,
    converter,
)
