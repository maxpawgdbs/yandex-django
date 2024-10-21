from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    template = "catalog/item_list.html"
    context = {
        "out": [
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
        ],
    }
    return render(request, template, context)


def item_detail(request, index):
    # return HttpResponse("<body>Подробно элемент</body>")
    template = "catalog/item.html"
    context = {}
    return render(request, template, context)


def item_detail_re(request, index):
    return HttpResponse("<body>" + index + "</body>")


def converter(request, index):
    return HttpResponse("<body>" + str(index) + "</body>")


__all__ = [
    item_detail,
    item_detail_re,
    item_list,
    converter,
]
