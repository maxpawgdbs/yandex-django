from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import django.contrib.auth.urls
from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path("download/", include("download.urls")),
    path("feedback/", include("feedback.urls")),
    path("auth/", include("users.urls")),
    path("auth/", include(django.contrib.auth.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += (path("_debug_/", include(debug_toolbar.urls)),)
