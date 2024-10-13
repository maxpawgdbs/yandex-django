import django.core.exceptions
import django.core.validators
import django.db


def custom_validator_words(value):
    if "превосходно" not in value.lower() and "роскошно" not in value.lower():
        raise django.core.exceptions.ValidationError("error")


def custom_validator_zero(value):
    if value <= 0 or value > 32767:
        raise django.core.exceptions.ValidationError("error")


def custom_validator_probeli(value):
    if len(value.split()) == 0:
        raise django.core.exceptions.ValidationError("error")


class Core(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        default="Название",
        help_text="Название",
        max_length=150,
        unique=True,
        validators=[
            django.core.validators.MinLengthValidator(2),
            custom_validator_probeli,
        ],
    )

    is_published = django.db.models.BooleanField(
        verbose_name="опубликовано",
        default=True,
        help_text="Статус публикации",
    )

    class Meta:
        abstract = True

    def clean(self):
        if isinstance(self.id, str) or self.id is not None and self.id < 1:
            raise django.core.exceptions.ValidationError(
                "ID не может быть отрицательным.",
            )


class Tag(Core):
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


class Category(Core):
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


class Item(Core):
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
