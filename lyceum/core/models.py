__all__ = ()
import django.core.exceptions
import django.core.validators
import django.db

import core.validators


class BaseModel(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        help_text="Введите название обьекта",
        max_length=150,
        unique=True,
        validators=[
            django.core.validators.MinLengthValidator(2),
            core.validators.custom_validator_spaces,
        ],
    )

    is_published = django.db.models.BooleanField(
        verbose_name="опубликовано",
        default=True,
        help_text="Отображать статус публикации",
    )

    class Meta:
        abstract = True


class ModelNormalizedNames(BaseModel):
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        default="Slag",
        help_text="Введите строку формата Slug",
        max_length=200,
    )

    normalized_name = django.db.models.CharField(
        verbose_name="нормализованные имена",
        help_text="Тут сохраняются нормализованные имена",
        max_length=150,
        unique=True,
        editable=False,
    )

    @classmethod
    def get_objects(cls):
        return cls.objects

    def clean(self):
        self.normalized_name = core.validators.normalization(self.name)
        if self.get_objects().count() > 1:
            qs = (
                self.get_objects()
                .exclude(pk=self.pk)
                .filter(
                    normalized_name=self.normalized_name,
                )
            )
            if qs.exists():
                raise django.core.exceptions.ValidationError(
                    "После нормализации имя не уникально",
                )

    class Meta:
        abstract = True
