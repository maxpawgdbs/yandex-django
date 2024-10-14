import django.core.exceptions
from django.test import Client, TestCase
from django.test import override_settings

import catalog.models


class MiddlewareOnLyceumTest(TestCase):
    @override_settings(ALLOW_REVERSE=True)
    def test_middleware(self):
        content = []
        for i in range(10):
            response = Client().get("/coffee/")
            content.append(response.content.decode("utf8"))
        self.assertEqual(content.count("Я кинйач"), 1)

    @override_settings(ALLOW_REVERSE=False)
    def test_middleware_off(self):
        content = []
        for i in range(10):
            response = Client().get("/coffee/")
            content.append(response.content.decode("utf8"))
        self.assertEqual(content.count("Я кинйач"), 0)


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="имя",
            slug="sluggg",
            weight=123,
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="имя",
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
                name="name",
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
                name="name",
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
            name="name",
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
            name="name",
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
                name="name",
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
                name="name",
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
                name="name",
                slug="slugg123",
                weight="lol",
            )
            self.category_test.full_clean()
            self.category_test.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            count,
        )

    def test_danila_nuchtoblyazatesti1(self):
        count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                id=-123,
                name="name",
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

    def test_danila_nuchtoblyazatesti2(self):
        count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                id="qwwqrrq",
                name="имя",
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


class UniqueNormalizeTest(TestCase):
    def test_tag_right_validator(self):
        count = catalog.models.Tag.objects.count()
        self.tag = catalog.models.Tag(
            is_published=True,
            name="name",
            slug="slugg123",
        )
        self.tag.full_clean()
        self.tag.save()

        self.tag1 = catalog.models.Tag(
            is_published=True,
            name="name1",
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
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.tag = catalog.models.Tag(
                is_published=True,
                name="name",
                slug="slugg123",
            )
            self.tag.full_clean()
            self.tag.save()

            self.tag1 = catalog.models.Tag(
                is_published=True,
                name="name",
                slug="slugg123",
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
            name="name",
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
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category = catalog.models.Category(
                is_published=True,
                name="name",
                slug="slugg123",
            )
            self.category.full_clean()
            self.category.save()

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
