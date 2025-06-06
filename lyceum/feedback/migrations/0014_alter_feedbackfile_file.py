# Generated by Django 4.2 on 2024-11-06 12:00

from django.db import migrations, models
import feedback.models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0013_alter_statuslog_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedbackfile",
            name="file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=feedback.models.FeedbackFile.get_upload_path,
            ),
        ),
    ]
