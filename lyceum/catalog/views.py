from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, index):
    return HttpResponse("<body>Подробно элемент</body>")


def item_detail_re(request, index):
    return HttpResponse("<body>" + index + "</body>")


def converter(request, index):
    return HttpResponse("<body>" + str(index) + "</body>")
