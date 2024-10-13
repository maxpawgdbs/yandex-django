from http import HTTPStatus

from django.test import Client, TestCase
from parametrize import parametrize


class StaticUrlCatalogTests(TestCase):
    def test_catalog(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parametrize(
        "test_input,expected",
        [
            (HTTPStatus.OK, Client().get("/catalog/123/").status_code),
            (HTTPStatus.NOT_FOUND, Client().get("/catalog/qwe/").status_code),
        ],
    )
    def test_catalog_index(self, test_input, expected):
        self.assertEqual(expected, test_input)

    @parametrize(
        "test_input,expected",
        [
            (HTTPStatus.OK, Client().get("/catalog/re/123/").status_code),
            (
                HTTPStatus.NOT_FOUND,
                Client().get("/catalog/re/-123/").status_code,
            ),
            (HTTPStatus.NOT_FOUND, Client().get("/catalog/re/0/").status_code),
            (
                HTTPStatus.NOT_FOUND,
                Client().get("/catalog/re/qwe/").status_code,
            ),
            (
                HTTPStatus.OK,
                Client().get("/catalog/re/123/qwe/qwe/qwe").status_code,
            ),
        ],
    )
    def test_catalog_re(self, test_input, expected):
        self.assertEqual(expected, test_input)

    @parametrize(
        "test_input,expected",
        [
            (
                HTTPStatus.OK,
                Client().get("/catalog/converter/123/").status_code,
            ),
            (
                HTTPStatus.NOT_FOUND,
                Client().get("/catalog/converter/0/").status_code,
            ),
            (
                HTTPStatus.NOT_FOUND,
                Client().get("/catalog/converter/-123/").status_code,
            ),
            (
                HTTPStatus.NOT_FOUND,
                Client().get("/catalog/converter/qwe/").status_code,
            ),
        ],
    )
    def test_converter(self, test_input, expected):
        self.assertEqual(expected, test_input)
