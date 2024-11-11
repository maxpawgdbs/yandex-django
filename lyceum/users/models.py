import django.contrib.auth.models
import django.db


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
    coffee_count = django.db.models.IntegerField(null=False, default=0)

    class Meta:
        verbose_name = "Дополнительные данные"
        verbose_name_plural = "Дополнительные данные"


__all__ = ()
