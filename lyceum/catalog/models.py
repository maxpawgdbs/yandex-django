import django.db
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

import catalog.validators
import core.models


class Tag(core.models.ModelNormalizedNames):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name[:15]


class Category(core.models.ModelNormalizedNames):
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


class Item(core.models.BaseModel):
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
    main_image = django.db.models.ImageField(
        verbose_name="Главная картинка",
        upload_to="items/main_image/",
        null=True,
        blank=True,
    )

    def get_image_300x300(self):
        return get_thumbnail(
            self.main_image,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.main_image:
            return mark_safe(
                f"<img src='{self.main_image.url}' width='50' height='50'>",
            )

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name[:15]


class ItemGalery(django.db.models.Model):
    images = django.db.models.ImageField(
        verbose_name="галерея",
        upload_to="items/galery/",
        null=True,
        blank=True,
    )
    item = django.db.models.ForeignKey(
        Item,
        related_name="photos",
        on_delete=django.db.models.CASCADE,
    )


__all__ = [
    Tag,
    Category,
    Item,
    ItemGalery,
]
