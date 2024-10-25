import http

import django.test
import django.urls


class StaticUrlAboutTests(django.test.TestCase):
    def test_about(self):
        url = django.urls.reverse("about:description")
        response = django.test.Client().get(url)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)


__all__ = (StaticUrlAboutTests,)
