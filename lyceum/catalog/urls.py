__all__ = ()
import django.urls

import catalog.converter
import catalog.views

django.urls.register_converter(catalog.converter.Converter, "converter")
app_name = "catalog"
urlpatterns = [
    django.urls.path("", catalog.views.item_list, name="item_list"),
    django.urls.path(
        "<int:index>/",
        catalog.views.item_detail,
        name="item_detail",
    ),
    django.urls.re_path(
        r"re/(?P<index>[1-9]\d*)/",
        catalog.views.item_detail_re,
        name="item_detail_re",
    ),
    django.urls.path(
        "converter/<converter:index>/",
        catalog.views.converter,
        name="converter",
    ),
    django.urls.path(
        "unverified/",
        catalog.views.unverified,
        name="unverified",
    ),
    django.urls.path("friday/", catalog.views.friday, name="friday"),
    django.urls.path("new/", catalog.views.new, name="new"),
]
