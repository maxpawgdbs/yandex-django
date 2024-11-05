# Generated by Django 4.2 on 2024-11-05 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0008_alter_feedback_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedbackText",
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
                ("text", models.TextField(verbose_name="Жалоба")),
                (
                    "feedback",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feedback.feedback",
                    ),
                ),
            ],
        ),
    ]