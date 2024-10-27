import django.core
import django.db
import django.dispatch
import django.utils.safestring
import sorl.thumbnail
import tinymce.models

import catalog.validators
import core.models


class ItemManager(django.db.models.Manager):
    def on_main(self):
        return (
            self.get_queryset()
            .filter(
                is_on_main=True,
                is_published=True,
                category__is_published=True,
            )
            .select_related("category", "main_image")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True,
                    ).only("name"),
                ),
            )
            .only("id", "name", "text", "category__name", "main_image__image")
        )

    def published(self):
        categorys = (
            catalog.models.Category.objects.filter(is_published=True)
            .values_list("name", flat=True)
            .order_by("name")
        )
        items = []
        for category in categorys:
            for item in (
                self.get_queryset()
                .filter(
                    is_published=True,
                    category__name=category,
                )
                .select_related("category", "main_image")
                .prefetch_related(
                    django.db.models.Prefetch(
                        "tags",
                        queryset=catalog.models.Tag.objects.filter(
                            is_published=True,
                        ).only("name"),
                    ),
                )
                .only(
                    "id",
                    "name",
                    "text",
                    "category__name",
                    "main_image__image",
                )
            ):
                items.append(item)
        new_categorys = []
        check = []
        for el in items:
            if el.category.name not in check:
                new_categorys.append(el.name)
                check.append(el.category.name)

        return new_categorys, items


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
    objects = ItemManager()
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
    is_on_main = django.db.models.BooleanField(
        verbose_name="на главной",
        default=False,
        help_text="Статус показа на главной странице",
    )
    tags = django.db.models.ManyToManyField(Tag)
    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
    )

    class Meta:
        ordering = ("name", "text", "id")
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
        return None

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
        related_name="images",
        on_delete=django.db.models.CASCADE,
        related_query_name="images",
    )

    def get_image_300x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.images.images,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.images:
            return django.utils.safestring.mark_safe(
                "<img src='{}' width='50' height='50'>".format(
                    self.images.images.url,
                ),
            )
        return None

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True


__all__ = (
    Tag,
    Category,
    Item,
    MainImage,
    ItemGalery,
)
