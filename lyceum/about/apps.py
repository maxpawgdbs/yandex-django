__all__ = ()

import django.apps


class AboutConfig(django.apps.AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "about"
    verbose_name = "О проекте"
