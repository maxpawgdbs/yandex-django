import django.core.exceptions
import django.core.validators
import django.db


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
