__all__ = ()
import django.urls

import download.views

app_name = "download"
urlpatterns = [
    django.urls.path(
        "<path:url>",
        download.views.download,
        name="download",
    ),
]
