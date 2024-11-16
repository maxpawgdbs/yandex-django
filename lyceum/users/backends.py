import django.conf
import django.contrib.auth.backends
import django.utils.timezone

import users.models


class MyBestBackendForDanila(django.contrib.auth.backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if "@" in username:
                normalized_email = (
                    users.models.ProxyUser.objects.normalize_email(
                        username,
                    )
                )
                user = users.models.ProxyUser.objects.by_mail(
                    email=normalized_email,
                )
            else:
                user = users.models.ProxyUser.objects.get(username=username)
        except users.models.ProxyUser.DoesNotExist:
            return None

        if user.check_password(password):
            user.profile.attempts_count = 0
            user.profile.save()
            return user

        user.profile.attempts_count += 1
        if (
            user.profile.attempts_count
            >= django.conf.settings.MAX_AUTH_ATTEMPTS
        ):
            user.profile.block_time = django.utils.timezone.now()
            user.profile.save()
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
