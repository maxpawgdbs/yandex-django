from django.urls import path, re_path, register_converter

import catalog.converter
import catalog.views

register_converter(catalog.converter.Converter, "converter")
app_name = "catalog"
urlpatterns = [
    path("", catalog.views.item_list, name="item_list"),
    path("<int:index>/", catalog.views.item_detail, name="item_detail"),
    re_path(
        r"re/(?P<index>[1-9]\d*)/",
        catalog.views.item_detail_re,
        name="item_detail_re",
    ),
    path(
        "converter/<converter:index>/",
        catalog.views.converter,
        name="converter",
    ),
]
