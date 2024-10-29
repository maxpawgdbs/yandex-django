import django.conf
import django.http


def download(request, image, filename):
    return django.http.FileResponse(
        open(
            f"{django.conf.settings.MEDIA_ROOT}/items/{image}/{filename}",
            "rb",
        ),
        as_attachment=True,
    )


__all__ = (download,)
