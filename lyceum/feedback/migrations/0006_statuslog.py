# Generated by Django 4.2 on 2024-11-04 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("feedback", "0005_feedback_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="StatusLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "from_status",
                    models.CharField(db_column="from", max_length=8),
                ),
                ("to_status", models.CharField(db_column="to", max_length=8)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
