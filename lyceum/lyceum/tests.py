from django.test import Client, TestCase, override_settings


class MiddlewareOnLyceumTest(TestCase):
    def test_middleware(self):
        for i in range(10):
            response = Client().get("/coffee/")
        self.assertEqual(response.content.decode("utf8"), "Я кинйач")


@override_settings(ALLOW_REVERSE=False)
class MiddlewareOffLyceumTest(TestCase):
    def test_middleware_off(self):
        for i in range(10):
            response = Client().get("/coffee/")
        self.assertEqual(response.content.decode("utf8"), "Я чайник")
