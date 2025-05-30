# Generated by Django 4.2 on 2024-11-22 14:36

import catalog.validators
import core.validators
import django.core.validators
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0016_alter_item_created_at_alter_item_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                help_text="Введите название обьекта",
                max_length=150,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    core.validators.custom_validator_spaces,
                ],
                verbose_name="название",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="normalized_name",
            field=models.CharField(
                editable=False,
                help_text="Тут сохраняются нормализованные имена",
                max_length=150,
                unique=True,
                verbose_name="нормализованные имена",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="weight",
            field=models.PositiveSmallIntegerField(
                help_text="Вес",
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(32767),
                ],
                verbose_name="вес",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(
                help_text="Введите название обьекта",
                max_length=150,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    core.validators.custom_validator_spaces,
                ],
                verbose_name="название",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="text",
            field=tinymce.models.HTMLField(
                help_text="Описание товара",
                validators=[
                    catalog.validators.ValidateMustContain(
                        "роскошно", "превосходно"
                    )
                ],
                verbose_name="текст",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(
                help_text="Введите название обьекта",
                max_length=150,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    core.validators.custom_validator_spaces,
                ],
                verbose_name="название",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="normalized_name",
            field=models.CharField(
                editable=False,
                help_text="Тут сохраняются нормализованные имена",
                max_length=150,
                unique=True,
                verbose_name="нормализованные имена",
            ),
        ),
    ]
