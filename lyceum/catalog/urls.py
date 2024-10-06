from catalog import converter, views

from django.urls import path, re_path, register_converter

register_converter(converter.Converter, "converter")

urlpatterns = [
    path("", views.item_list),
    path("<int:index>/", views.item_detail),
    re_path(r"re/(?P<index>[1-9]\d*)/", views.item_detail_re),
    path("converter/<converter:index>/", views.converter, name="converter"),
]
