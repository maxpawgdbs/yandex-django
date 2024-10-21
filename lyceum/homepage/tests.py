from http import HTTPStatus

from django.shortcuts import reverse
from django.test import Client, TestCase
from parametrize import parametrize


class StaticUrlHomepageTest(TestCase):
    def test_homepage(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parametrize(
        "test_input,expected",
        [
            (HTTPStatus.IM_A_TEAPOT, Client().get("/coffee/").status_code),
            ("Я чайник", Client().get("/coffee/").content.decode("utf8")),
        ],
    )
    def test_coffee(self, test_input, expected):
        self.assertEqual(expected, test_input)

    def test_reverse(self):
        url = reverse("homepage:home")
        self.assertEqual(url, "/")


__all__ = [
    StaticUrlHomepageTest,
]
