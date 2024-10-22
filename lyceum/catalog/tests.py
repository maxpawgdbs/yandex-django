from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse
from parametrize import parametrize


class StaticUrlCatalogTests(TestCase):
    def test_catalog(self):
        url = reverse("catalog:item_list")
        response = Client().get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parametrize(
        "test_input,expected",
        [
            (
                HTTPStatus.OK,
                Client()
                .get(reverse("catalog:item_detail", args=[123]))
                .status_code,
            ),
            (HTTPStatus.NOT_FOUND, Client().get("/catalog/qwe/").status_code),
        ],
    )
    def test_catalog_index(self, test_input, expected):
        self.assertEqual(expected, test_input)

    @parametrize(
        "test_input,expected",
        [
            (
                HTTPStatus.OK,
                Client()
                .get(reverse("catalog:item_detail_re", args=[123]))
                .status_code,
            ),
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
                Client()
                .get(reverse("catalog:converter", args=[123]))
                .status_code,
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


__all__ = [
    StaticUrlCatalogTests,
]
