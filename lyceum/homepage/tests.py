import http

import django.test
import django.urls


class StaticUrlHomepageTest(django.test.TestCase):
    def test_homepage(self):
        url = django.urls.reverse("homepage:home")
        response = django.test.Client().get(url)
        self.assertEqual(http.HTTPStatus.OK, response.status_code)

    def test_coffee(self):
        url = django.urls.reverse("homepage:teapot")
        response = django.test.Client().get(url)
        self.assertEqual(http.HTTPStatus.IM_A_TEAPOT, response.status_code)
        self.assertEqual("Я чайник", response.content.decode("utf8"))


__all__ = (StaticUrlHomepageTest,)
