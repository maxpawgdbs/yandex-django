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

__all__ = (
    app_name,
    urlpatterns,
)
