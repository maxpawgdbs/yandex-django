import django.db
import django.core
import django.utils.safestring
import sorl.thumbnail
import tinymce.models

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
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(32767),
        ],
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name[:15]


class Item(core.models.BaseModel):
    text = tinymce.models.HTMLField(
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


class MainImage(django.db.models.Model):
    image = django.db.models.ImageField(
        verbose_name="галерея",
        upload_to="items/main_image/",
        null=True,
        blank=True,
    )
    item = django.db.models.OneToOneField(
        Item,
        related_name="main_image",
        on_delete=django.db.models.CASCADE,
    )

    def get_image_300x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.main_image.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.main_image:
            return django.utils.safestring.mark_safe(
                "<img src='{}' width='50' height='50'>".format(
                    self.main_image.image.url,
                ),
            )

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True


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

    def get_image_300x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.photos.images,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.photos:
            return django.utils.safestring.mark_safe(
                "<img src='{}' width='50' height='50'>".format(
                    self.photos.images.url,
                ),
            )

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True


__all__ = (
    Tag,
    Category,
    Item,
    MainImage,
    ItemGalery,
)
