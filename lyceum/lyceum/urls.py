from django.contrib import admin
from django.urls import include, path

import lyceum.settings

if lyceum.settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
]

if lyceum.settings.DEBUG:
    urlpatterns += (path("_debug_/", include(debug_toolbar.urls)),)
