from django.urls import path
from catalog import views

urlpatterns = [
    path("", views.item_list),
    path("<int:index>/", views.item_detail),
]
