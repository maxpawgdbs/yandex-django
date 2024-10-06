from django.contrib import admin
from django.urls import include, path

from lyceum import settings

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += (path("_debug_/", include(debug_toolbar.urls)),)
