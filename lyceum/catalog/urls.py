from catalog import views
from django.http import Http404
from django.urls import path, re_path, register_converter


class Converter:
    regex = r"\d+"

    def to_python(self, value):
        if int(value) <= 0:
            raise Http404
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(Converter, "converter")

urlpatterns = [
    path("", views.item_list),
    path("<int:index>/", views.item_detail),
    re_path(r"re/(?P<index>\d+)/", views.item_detail_re),
    path("converter/<converter:index>/", views.converter, name="converter"),
]
