import django.conf
import django.contrib.auth.backends

import users.models


class MyBestBackendForDanila(django.contrib.auth.backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            normalized_email = users.models.ProxyUser.objects.normalize_email(
                username,
            )
            user = users.models.ProxyUser.objects.by_mail(
                email=normalized_email,
            )
        except users.models.ProxyUser.DoesNotExist:
            try:
                user = users.models.ProxyUser.objects.get(username=username)
            except users.models.ProxyUser.DoesNotExist:
                return None

        if user.check_password(password):
            user.profile.attempt_count = 0
            user.profile.save()
            return user

        user.profile.attempt_count += 1
        if (
            user.profile.attempt_count
            >= django.conf.settings.MAX_AUTH_ATTEMPTS
        ):
            user.is_active = False
            user.save()
            django.core.mail.send_mail(
                subject=user.username,
                message="У вас неделя на восстановление "
                "профиля на нашем сайте\n"
                f"вот ссылка: 127.0.0.1/users/activated/{user.username}",
                from_email=django.conf.settings.DJANGO_MAIL,
                recipient_list=[
                    user.email,
                ],
                fail_silently=False,
            )

        user.profile.save()

        return None


__all__ = ()
