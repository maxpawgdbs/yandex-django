from django.test import Client, TestCase
from django.test import override_settings


class MiddlewareOnLyceumTest(TestCase):
    @override_settings(ALLOW_REVERSE=True)
    def test_middleware(self):
        content = []
        for i in range(10):
            response = Client().get("/coffee/")
            content.append(response.content.decode("utf8"))
        self.assertEqual(content.count("Я кинйач"), 1)

    @override_settings(ALLOW_REVERSE=False)
    def test_middleware_off(self):
        content = []
        for i in range(10):
            response = Client().get("/coffee/")
            content.append(response.content.decode("utf8"))
        self.assertEqual(content.count("Я кинйач"), 0)
