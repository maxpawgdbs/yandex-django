import django.urls

import homepage.views

app_name = "homepage"
urlpatterns = [
    django.urls.path("", homepage.views.home, name="home"),
    django.urls.path("coffee/", homepage.views.teapot, name="teapot"),
]

__all__ = (
    app_name,
    urlpatterns,
)
