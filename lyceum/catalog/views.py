import django.http
import django.shortcuts

import catalog.models


def item_list(request):
    template = "catalog/item_list.html"
    items = catalog.models.Item.objects.filter(is_published=True).order_by(
        "category__name",
    )
    context = {
        "items": items,
    }
    return django.shortcuts.render(request, template, context)


def item_detail(request, index):
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item,
        pk=index,
    )
    if (not item.is_published) and (not item.is_on_main):
        raise django.http.Http404
    context = {
        "item": item,
    }
    template = "catalog/item.html"
    return django.shortcuts.render(request, template, context)


def item_detail_re(request, index):
    return django.http.HttpResponse("<body>" + index + "</body>")


def converter(request, index):
    return django.http.HttpResponse("<body>" + str(index) + "</body>")


__all__ = (
    item_detail,
    item_detail_re,
    item_list,
    converter,
)
