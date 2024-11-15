import sys

import django.contrib.auth.models
import django.db

if "makemigrations" not in sys.argv and "migrate" not in sys.argv:
    user = django.contrib.auth.models.User
    user._meta.get_field("email")._unique = True


class Profile(django.db.models.Model):
    user = django.db.models.OneToOneField(
        django.contrib.auth.models.User,
        on_delete=django.db.models.CASCADE,
        related_name="profile",
        related_query_name="profile",
    )
    birthday = django.db.models.DateField(null=True, blank=True)
    image = django.db.models.ImageField(
        upload_to="users/images/",
        null=True,
        blank=True,
    )
    coffee_count = django.db.models.PositiveIntegerField(null=False, default=0)

    class Meta:
        verbose_name = "Дополнительные данные"
        verbose_name_plural = "Дополнительные данные"


class ProxyManager(django.db.models.Manager):
    def by_email(self, email):
        return self.get(**{self.model.EMAIL_FIELD: email})

    def active(self):
        users = self.get_queryset()
        return users.filter(is_active=True).select_related("profile")


class ProxyUser(django.contrib.auth.models.User):
    objects = ProxyManager()

    class Meta:
        proxy = True


__all__ = ()
