from http import HTTPStatus

from django.shortcuts import reverse
from django.test import Client, TestCase
import django.urls
from parametrize import parametrize


class StaticUrlHomepageTest(TestCase):
    def test_homepage(self):
        url = reverse("homepage:home")
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        with self.assertRaises(django.urls.NoReverseMatch):
            url = reverse("homepage:main")
            response = Client().get(url)

    @parametrize(
        "test_input,expected",
        [
            (HTTPStatus.IM_A_TEAPOT, Client().get("/coffee/").status_code),
            ("Я чайник", Client().get("/coffee/").content.decode("utf8")),
        ],
    )
    def test_coffee(self, test_input, expected):
        self.assertEqual(expected, test_input)


__all__ = [
    StaticUrlHomepageTest,
]
