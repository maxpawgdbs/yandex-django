from http import HTTPStatus

from django.test import Client, TestCase


class StaticUrlAboutTests(TestCase):
    def test_about(self):
        response = Client().get("/about/")
        self.assertEqual(response.status_code, HTTPStatus.OK)


__all__ = [
    StaticUrlAboutTests,
]
