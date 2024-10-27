import django.db
import django.http
import django.shortcuts

import catalog.models


def item_list(request):
    template = "catalog/item_list.html"
    categorys, items = catalog.models.Item.objects.published()
    context = {
        "items": items,
        "categorys": categorys,
    }
    return django.shortcuts.render(request, template, context)


def item_detail(request, index):
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.filter(is_published=True)
        .select_related("category", "main_image")
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
