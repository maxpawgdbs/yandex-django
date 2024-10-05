from django.test import Client, TestCase


class StaticUrlCatalogTests(TestCase):
    def test_catalog(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_right_index(self):
        response = Client().get("/catalog/123/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_wrong_index(self):
        response = Client().get("/catalog/qwe/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_right_index(self):
        response = Client().get("/catalog/re/123/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_re_wrong_index(self):
        response = Client().get("/catalog/re/-123/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_zero_index(self):
        response = Client().get("/catalog/re/0/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_text_index(self):
        response = Client().get("/catalog/re/qwe/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_right_index_with_text(self):
        response = Client().get("/catalog/re/123/qwe/qwe/qwe/")
        self.assertEqual(response.status_code, 200)

    def test_converter_right_index(self):
        response = Client().get("/catalog/converter/123/")
        self.assertEqual(response.status_code, 200)

    def test_converter_wrong_index(self):
        response = Client().get("/catalog/converter/0/")
        self.assertEqual(response.status_code, 404)

    def test_converter_text_index(self):
        response = Client().get("/catalog/converter/qwe/")
        self.assertEqual(response.status_code, 404)
