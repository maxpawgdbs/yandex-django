import django.db

import catalog.validators

import core.models


class Tag(core.models.Core):
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


class Category(core.models.Core):
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
            catalog.validators.custom_validator_zero,
        ],
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name[:15]


class Item(core.models.Core):
    text = django.db.models.TextField(
        verbose_name="текст",
        default="Превосходно",
        help_text="Описание товара",
        validators=[
            catalog.validators.ValidateMustContain(
                "роскошно",
                "превосходно",
            ),
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
