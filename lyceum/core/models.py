import django.db


class Core(django.db.models.Model):
    name = django.db.models.TextField(
        "Название",
        default="Название",
        help_text="Название",
        validators=[
            django.core.validators.MaxLengthValidator(150),
        ],
        max_length=150,
        unique=True,
    )

    is_published = django.db.models.BooleanField(
        "Опубликовано",
        default=True,
        help_text="Статус публикации",
    )

    class Meta:
        abstract = True
