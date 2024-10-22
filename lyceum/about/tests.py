from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse


class StaticUrlAboutTests(TestCase):
    def test_about(self):
        url = reverse("about:description")
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


__all__ = [
    StaticUrlAboutTests,
]
