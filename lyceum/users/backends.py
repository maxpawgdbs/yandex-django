import django.contrib.auth
import django.contrib.auth.backends


class MyBestBackendForDanila(django.contrib.auth.backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = django.contrib.auth.get_user_model()
        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            try:
                user = user_model.objects.get(username=username)
            except user_model.DoesNotExist:
                return None

        if user.check_password(password):
            return user

        return None


__all__ = ()
