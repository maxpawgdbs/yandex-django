import http

import django.core.exceptions
import django.db
import django.test
import django.urls
import parametrize

import catalog.models


class StaticUrlCatalogTests(django.test.TestCase):
    fixtures = ["fixtures/data.json"]

    def test_catalog(self):
        url = django.urls.reverse("catalog:item_list")
        response = django.test.Client().get(url)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_catalog_context(self):
        url = django.urls.reverse("catalog:item_list")
        response = django.test.Client().get(url)
        context = response.context
        items = context["items"]
        self.assertIn("items", context)
        self.assertEqual(items.count(), 9)
        self.assertIsInstance(context["items"], django.db.models.QuerySet)
        self.assertIsInstance(context["item"], catalog.models.Item)
        self.assertEqual(len(response.context["items"]), 9)

    @parametrize.parametrize(
        "expected, test_input",
        [
            (http.HTTPStatus.OK, ("catalog:item_detail", [11])),
        ],
    )
    def test_catalog_right_index(self, expected, test_input):
        url = django.urls.reverse(test_input[0], args=test_input[1])
        response = django.test.Client().get(url)
        self.assertEqual(expected, response.status_code)

    @parametrize.parametrize(
        "expected, test_input",
        [
            (
                http.HTTPStatus.NOT_FOUND,
                ("catalog:item_detail", ["qwe"]),
            ),
            (
                http.HTTPStatus.NOT_FOUND,
                ("catalog:item_detail", [-1]),
            ),
        ],
    )
    def test_catalog_wrong_index(self, expected, test_input):
        with self.assertRaises(django.urls.exceptions.NoReverseMatch):
            url = django.urls.reverse(test_input[0], args=test_input[1])
            response = django.test.Client().get(url)
            self.assertEqual(expected, response.status_code)

    @parametrize.parametrize(
        "expected, test_input",
        [
            (
                http.HTTPStatus.OK,
                ("catalog:item_detail_re", [123]),
            ),
        ],
    )
    def test_catalog_right_re(self, expected, test_input):
        url = django.urls.reverse(test_input[0], args=test_input[1])
        response = django.test.Client().get(url)
        self.assertEqual(expected, response.status_code)

    @parametrize.parametrize(
        "expected, test_input",
        [
            (
                http.HTTPStatus.NOT_FOUND,
                ("catalog:item_detail_re", [-123]),
            ),
            (
                http.HTTPStatus.NOT_FOUND,
                ("catalog:item_detail_re", [0]),
            ),
            (
                http.HTTPStatus.NOT_FOUND,
                ("catalog:item_detail_re", ["qwe"]),
            ),
        ],
    )
    def test_catalog_wrong_re(self, expected, test_input):
        with self.assertRaises(django.urls.exceptions.NoReverseMatch):
            url = django.urls.reverse(test_input[0], args=test_input[1])
            response = django.test.Client().get(url)
            self.assertEqual(expected, response.status_code)

    @parametrize.parametrize(
        "expected, test_input",
        [
            (
                http.HTTPStatus.OK,
                ("catalog:converter", [123]),
            ),
        ],
    )
    def test_converter_right(self, expected, test_input):
        url = django.urls.reverse(test_input[0], args=test_input[1])
        response = django.test.Client().get(url)
        self.assertEqual(expected, response.status_code)

    @parametrize.parametrize(
        "expected, test_input",
        [
            (
                http.HTTPStatus.NOT_FOUND,
                ("catalog:converter", [0]),
            ),
            (
                http.HTTPStatus.NOT_FOUND,
                ("catalog:converter", [-123]),
            ),
            (
                http.HTTPStatus.NOT_FOUND,
                ("catalog:converter", ["qwe"]),
            ),
        ],
    )
    def test_converter_wrong(self, expected, test_input):
        with self.assertRaises(django.urls.exceptions.NoReverseMatch):
            url = django.urls.reverse(test_input[0], args=test_input[1])
            response = django.test.Client().get(url)
            self.assertEqual(expected, response.status_code)


class ModelsTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="имя123",
            slug="sluggg",
            weight=123,
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="имя123",
            slug="sluggg",
        )

    def test_create_item(self):
        count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
            name="name",
            category=self.category,
            text="Превосходно",
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTest.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            count + 1,
        )

    def test_text_validator(self):
        count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                id=1,
                name="name",
                category=self.category,
                text="фигня",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            count,
        )

    def test_text_validator2(self):
        count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                id=1,
                name="name",
                category=self.category,
                text=",роскошный1",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            count,
        )

    def test_slug_validator(self):
        count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category_test = catalog.models.Category(
                is_published=True,
                name="name1",
                slug="фигня",
                weight=123,
            )
            self.category_test.full_clean()
            self.category_test.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            count,
        )

    def test_slug_validator2(self):
        count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category_test = catalog.models.Category(
                is_published=True,
                name="name2",
                slug="123ф",
                weight=123,
            )
            self.category_test.full_clean()
            self.category_test.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            count,
        )

    def test_right_slug_validator(self):
        count = catalog.models.Category.objects.count()
        self.category_test = catalog.models.Category(
            is_published=True,
            name="name3",
            slug="slug123",
            weight=123,
        )
        self.category_test.full_clean()
        self.category_test.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            count + 1,
        )

    def test_create_category(self):
        count = catalog.models.Category.objects.count()
        self.category_test = catalog.models.Category(
            is_published=True,
            name="name4lol",
            slug="slug123",
            weight=123,
        )
        self.category_test.full_clean()
        self.category_test.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            count + 1,
        )

    def test_zero_validator(self):
        count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category_test = catalog.models.Category(
                is_published=True,
                name="name5",
                slug="slugg123",
                weight=0,
            )
            self.category_test.full_clean()
            self.category_test.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            count,
        )

    def test_weight_validator(self):
        count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category_test = catalog.models.Category(
                is_published=True,
                name="name6",
                slug="slugg123",
                weight=-123,
            )
            self.category_test.full_clean()
            self.category_test.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            count,
        )

    def test_wieght_text_validator(self):
        count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category_test = catalog.models.Category(
                is_published=True,
                name="name7",
                slug="slugg123",
                weight="lol",
            )
            self.category_test.full_clean()
            self.category_test.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            count,
        )

    def test_danila_nuchtozatesti1(self):
        count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                id=-123,
                name="name8",
                category=self.category,
                text="Роскошно",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            count,
        )

    def test_danila_nuchtozatesti2(self):
        count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                id="qwwqrrq",
                name="имя10",
                category=self.category,
                text="Превосходно",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            count,
        )


class UniqueNormalizeTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="имя123",
            slug="sluggg",
            weight=123,
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="имя123",
            slug="sluggg",
        )

    def test_tag_right_validator(self):
        count = catalog.models.Tag.objects.count()
        self.tag = catalog.models.Tag(
            is_published=True,
            name="name123",
            slug="slugg123",
        )
        self.tag.full_clean()
        self.tag.save()

        self.tag1 = catalog.models.Tag(
            is_published=True,
            name="name1lest",
            slug="slugg123",
        )
        self.tag1.full_clean()
        self.tag1.save()

        self.assertEqual(
            catalog.models.Tag.objects.count(),
            count + 2,
        )

    def test_tag_wrong_validator(self):
        count = catalog.models.Tag.objects.count()
        self.tag = catalog.models.Tag(
            is_published=True,
            name="рoka",
            slug="slugg123",
        )
        self.tag.full_clean()
        self.tag.save()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.tag1 = catalog.models.Tag(
                is_published=True,
                name="poka..",
                slug="ahihlga",
            )
            self.tag1.full_clean()
            self.tag1.save()

        self.assertEqual(
            catalog.models.Tag.objects.count(),
            count + 1,
        )

    def test_category_right_validator(self):
        count = catalog.models.Category.objects.count()
        self.category = catalog.models.Category(
            is_published=True,
            name="name123",
            slug="slugg123",
        )
        self.category.full_clean()
        self.category.save()

        self.category1 = catalog.models.Category(
            is_published=True,
            name="name1",
            slug="slugg123",
        )
        self.category1.full_clean()
        self.category1.save()

        self.assertEqual(
            catalog.models.Category.objects.count(),
            count + 2,
        )

    def test_category_wrong_validator(self):
        count = catalog.models.Category.objects.count()
        self.category = catalog.models.Category(
            is_published=True,
            name="name",
            slug="slugg123",
        )
        self.category.full_clean()
        self.category.save()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category1 = catalog.models.Category(
                is_published=True,
                name="name",
                slug="slugg123",
            )
            self.category1.full_clean()
            self.category1.save()

        self.assertEqual(
            catalog.models.Category.objects.count(),
            count + 1,
        )


__all__ = (
    StaticUrlCatalogTests,
    ModelsTest,
    UniqueNormalizeTest,
)
