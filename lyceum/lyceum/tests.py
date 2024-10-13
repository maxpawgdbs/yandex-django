import catalog.models

import django.core.exceptions
from django.test import Client, TestCase
from django.test import override_settings


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
            id=1,
            name="name",
            category=self.category,
            text="Превосходно",
        )
        self.item.tags.add(ModelsTest.tag)
        self.item.full_clean()
        self.item.save()
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

    def test_slug_validator(self):
        count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category_test = catalog.models.Category(
                id=1,
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
                id=1,
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
