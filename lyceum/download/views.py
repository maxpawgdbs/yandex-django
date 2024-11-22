__all__ = ()
import django.conf
import django.http


def download(request, url):
    return django.http.FileResponse(
        open(
            django.conf.settings.MEDIA_ROOT / url,
            "rb",
        ),
        as_attachment=True,
    )
