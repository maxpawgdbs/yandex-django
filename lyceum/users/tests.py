from django.contrib.auth.models import User
import django.test
import django.urls

import users.models


class TestUser(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.username = "test"
        cls.email = "test@test.test"
        cls.password = "thebestpassword_17112008"
        cls.user = User.objects.create_user(
            cls.username,
            cls.email,
            cls.password,
        )
        cls.profile = users.models.Profile.objects.create(user=cls.user)

    def test_login_username(self):
        response = self.client.post(
            django.urls.reverse("users:login"),
            {
                "username": self.username,
                "password": self.password,
            },
        )
        self.assertRedirects(response, django.urls.reverse("users:profile"))

    def test_login_email(self):
        response = self.client.post(
            django.urls.reverse("users:login"),
            {
                "username": self.email,
                "password": self.password,
            },
        )
        self.assertRedirects(response, django.urls.reverse("users:profile"))

    def test_login_error(self):
        response = self.client.post(
            django.urls.reverse("users:login"),
            {
                "username": "test_not_found",
                "password": self.password,
            },
        )
        self.assertContains(
            response,
            (
                "Пожалуйста, введите правильные имя пользователя и пароль."
                " Оба поля могут быть чувствительны к регистру."
            ),
        )


__all__ = ()
