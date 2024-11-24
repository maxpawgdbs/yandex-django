__all__ = ()
from django.contrib.auth.models import User
import django.test
import django.urls


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
        self.assertEqual(200, response.status_code)

    def test_normalize_email(self):
        response = self.client.post(
            django.urls.reverse("users:login"),
            {
                "username": "test+dgdssdg@test.test",
                "password": self.password,
            },
        )
        self.assertRedirects(response, django.urls.reverse("users:profile"))

    @django.test.override_settings(MAX_AUTH_ATTEMPTS=3)
    def test_attempts(self):
        for _ in range(4):
            self.client.post(
                django.urls.reverse("users:login"),
                {
                    "username": self.email,
                    "password": "dsgfsgsd",
                },
            )

        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)

        self.client.get(
            django.urls.reverse("users:activated", args=[self.user.username]),
        )
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)
