import django.db


class Core(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        default="Название",
        help_text="Название",
        max_length=150,
        unique=True,
    )

    is_published = django.db.models.BooleanField(
        verbose_name="опубликовано",
        default=True,
        help_text="Статус публикации",
    )

    class Meta:
        abstract = True
