# Generated by Django 4.2 on 2024-10-27 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_item_is_on_main_squashed_0008_alter_item_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="normalized_name",
            field=models.CharField(
                default="нормализуйся",
                editable=False,
                help_text="Тут сохраняются нормализованные имена",
                max_length=150,
                verbose_name="нормализованные имена",
            ),
        ),
        migrations.AlterField(
            model_name="itemgalery",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="catalog.item",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="normalized_name",
            field=models.CharField(
                default="нормализуйся",
                editable=False,
                help_text="Тут сохраняются нормализованные имена",
                max_length=150,
                verbose_name="нормализованные имена",
            ),
        ),
    ]
