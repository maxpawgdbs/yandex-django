from django.test import Client, TestCase


class StaticUrlCatalogTests(TestCase):
    def test_catalog(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_right_index(self):
        response = Client().get("/catalog/123/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_wrong_inde(self):
        response = Client().get("/catalog/qwe/")
        self.assertEqual(response.status_code, 404)
