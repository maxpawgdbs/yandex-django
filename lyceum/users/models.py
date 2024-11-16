import sys

import django.contrib.auth.base_user
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
    attempts_count = django.db.models.IntegerField(default=0)
    block_time = django.db.models.DateTimeField(
        default="1111-11-11 11:11:11.1111",
    )

    class Meta:
        verbose_name = "Дополнительные данные"
        verbose_name_plural = "Дополнительные данные"


class ProxyManager(django.contrib.auth.base_user.BaseUserManager):
    @classmethod
    def normalize_email(cls, email):
        email = super().normalize_email(email)
        email = email or ""
        email = email.lower()
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            i = email_name.find("+")
            if i != -1:
                email_name = email_name[:i]

            if domain_part == "gmail.com":
                email_name = email_name.replace(".", "")

            if domain_part in ["ya.ru", "yandex.ru"]:
                email_name = email_name.replace(".", "-")
                domain_part = "yandex.ru"

            email = email_name + "@" + domain_part

        return email

    def by_mail(self, email):
        return self.get(
            **{self.model.EMAIL_FIELD: self.normalize_email(email)},
        )

    def active(self):
        users = self.get_queryset()
        return users.filter(is_active=True).select_related("profile")


class ProxyUser(django.contrib.auth.models.User):
    objects = ProxyManager()

    class Meta:
        proxy = True


__all__ = ()
