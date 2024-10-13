import re

from core import models

import django.core.exceptions
import django.core.validators
import django.db


def custom_validator_words(value):
    if "превосходно" not in value.lower() and "роскошно" not in value.lower():
        raise django.core.exceptions.ValidationError("error")


def custom_validator_right_string(value):
    if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
        raise django.core.exceptions.ValidationError("error")


def custom_validator_zero(value):
    if value == 0:
        raise django.core.exceptions.ValidationError("error")


class Tag(models.Core):
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        default="Slag",
        help_text="Слаг",
        max_length=200,
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name[:15]


class Category(models.Core):
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        default="Slag",
        help_text="Слаг",
        max_length=200,
    )
    weight = django.db.models.PositiveSmallIntegerField(
        verbose_name="вес",
        default=100,
        help_text="Вес",
        validators=[
            custom_validator_zero,
        ],
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name[:15]


class Item(models.Core):
    text = django.db.models.TextField(
        verbose_name="текст",
        default="Превосходно",
        help_text="Описание товара",
        validators=[
            custom_validator_words,
        ],
    )
    tags = django.db.models.ManyToManyField(Tag)
    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:15]
