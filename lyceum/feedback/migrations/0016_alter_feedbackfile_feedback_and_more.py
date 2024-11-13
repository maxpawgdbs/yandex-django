# Generated by Django 4.2 on 2024-11-06 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("feedback", "0015_alter_feedbackfile_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedbackfile",
            name="feedback",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="feedback.feedback",
            ),
        ),
        migrations.AlterField(
            model_name="feedbacktext",
            name="feedback",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                to="feedback.feedback",
            ),
        ),
        migrations.AlterField(
            model_name="statuslog",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]