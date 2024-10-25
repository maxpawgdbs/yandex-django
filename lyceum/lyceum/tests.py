import django.test
import django.urls


class MiddlewareOnLyceumTest(django.test.TestCase):
    @django.test.override_settings(ALLOW_REVERSE=True)
    def test_middleware(self):
        content = []
        url = django.urls.reverse("homepage:teapot")
        for i in range(10):
            response = django.test.Client().get(url)
            content.append(response.content.decode("utf8"))
        self.assertEqual(content.count("Я кинйач"), 1)

    @django.test.override_settings(ALLOW_REVERSE=False)
    def test_middleware_off(self):
        content = []
        url = django.urls.reverse("homepage:teapot")
        for i in range(10):
            response = django.test.Client().get(url)
            content.append(response.content.decode("utf8"))
        self.assertEqual(content.count("Я кинйач"), 0)


__all__ = (MiddlewareOnLyceumTest,)
