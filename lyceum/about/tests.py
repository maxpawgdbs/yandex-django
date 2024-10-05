from django.test import Client, TestCase


class StaticUrlAboutTests(TestCase):
    def test_about(self):
        response = Client().get("/about/")
        self.assertEqual(response.status_code, 200)
