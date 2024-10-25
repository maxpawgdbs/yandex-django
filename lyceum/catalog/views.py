import django.http
import django.shortcuts


def item_list(request):
    template = "catalog/item_list.html"
    items = [
        {
            "id": 1,
            "name": "Предмет 1",
            "is_published": True,
            "text": "Роскошно",
            "img": "thing1.jpg",
        },
        {
            "id": 2,
            "name": "Предмет 2",
            "is_published": False,
            "text": "Превосходно",
            "img": "thing2.jpg",
        },
        {
            "id": 3,
            "name": "Предмет 3",
            "is_published": True,
            "text": "Роскошно Превосходно",
            "img": "thing3.jpg",
        },
    ]
    context = {"items": []}
    for el in items:
        if el["is_published"]:
            context["items"].append(el)
    return django.shortcuts.render(request, template, context)


def item_detail(request, index):
    template = "catalog/item.html"
    return django.shortcuts.render(request, template)


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
