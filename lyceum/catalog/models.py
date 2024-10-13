from core import models

import django.core.exceptions
import django.core.validators
import django.db


def custom_validator_words(value):
    text = value.lower().split()
    a = True
    words = [
        "роскошно",
        "роскошное",
        "роскошный",
        "роскошная",
        "роскошные",
        "превосходно",
        "превосходный",
        "превосходная",
        "превосходное",
        "превосходные",
    ]
    chars = "()!?,."
    for i in range(len(text)):
        word = text[i]
        for el in words:
            if el in word:
                index = word.find(el)
                i0 = index - 1
                i1 = index + len(el)
                if (i0 == -1 or word[i0] in chars) and (
                    i1 == len(word) or word[i1] in chars
                ):
                    a = False
                    break
        if not a:
            break
    if a:
        raise django.core.exceptions.ValidationError("error")


def custom_validator_zero(value):
    if value <= 0 or value > 32767:
        raise django.core.exceptions.ValidationError("error")


class Tag(models.Core):
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        default="Slag",
        help_text="Слаг",
        max_length=200,
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

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
        verbose_name = "категория"
        verbose_name_plural = "категории"

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
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name[:15]
