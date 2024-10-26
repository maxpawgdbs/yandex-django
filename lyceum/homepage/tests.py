import http

import django.test
import django.urls


class StaticUrlHomepageTest(django.test.TestCase):
    fixtures = ["fixtures/data.json"]

    def test_homepage(self):
        url = django.urls.reverse("homepage:home")
        response = django.test.Client().get(url)
        items = response.context["items"][0]
        self.assertEqual(items.count(), 8)
        self.assertIn("items", response.context)

    def test_coffee(self):
        url = django.urls.reverse("homepage:teapot")
        response = django.test.Client().get(url)
        self.assertEqual(http.HTTPStatus.IM_A_TEAPOT, response.status_code)
        self.assertEqual("Я чайник", response.content.decode("utf8"))


__all__ = (StaticUrlHomepageTest,)
