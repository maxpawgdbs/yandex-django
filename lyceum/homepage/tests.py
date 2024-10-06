from http import HTTPStatus

from django.test import Client, TestCase


class StaticUrlHomepageTest(TestCase):
    def test_homepage(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_coffee_status(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)

    def test_coffee_text(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.content.decode("utf8"), "Я чайник")
