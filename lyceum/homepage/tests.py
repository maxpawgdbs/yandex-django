import http

import django.test
import django.urls


class StaticUrlHomepageTest(django.test.TestCase):
    fixtures = ["fixtures/data.json"]

    def test_homepage(self):
        url = django.urls.reverse("homepage:home")
        response = django.test.Client().get(url)
        self.assertEqual(http.HTTPStatus.OK, response.status_code)
        context = response.context
        items = context["items"]
        self.assertNotIn("is_published", items[0].__dict__)
        self.assertNotIn("is_on_main", items[0].__dict__)
        self.assertNotIn("images", items[0].__dict__)

    @django.test.override_settings(ALLOW_REVERSE=False)
    def test_coffee(self):
        url = django.urls.reverse("homepage:teapot")
        response = django.test.Client().get(url)
        self.assertEqual(http.HTTPStatus.IM_A_TEAPOT, response.status_code)
        self.assertEqual("Я чайник", response.content.decode("utf8"))


__all__ = (StaticUrlHomepageTest,)
