from django.http import Http404, HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, index):
    return HttpResponse("<body>Подробно элемент</body>")


def item_detail_re(request, index):
    if index == "0":
        raise Http404
    return HttpResponse("<body>" + index + "</body>")


def converter(request, index):
    return HttpResponse("<body>" + str(index) + "</body>")
