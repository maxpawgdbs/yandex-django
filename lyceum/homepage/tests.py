from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse
from parametrize import parametrize


class StaticUrlHomepageTest(TestCase):
    def test_homepage(self):
        url = reverse("homepage:home")
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parametrize(
        "test_input,expected",
        [
            (
                HTTPStatus.IM_A_TEAPOT,
                Client().get(reverse("homepage:teapot")).status_code,
            ),
            (
                "Я чайник",
                Client()
                .get(reverse("homepage:teapot"))
                .content.decode("utf8"),
            ),
        ],
    )
    def test_coffee(self, test_input, expected):
        self.assertEqual(expected, test_input)


__all__ = [
    StaticUrlHomepageTest,
]
