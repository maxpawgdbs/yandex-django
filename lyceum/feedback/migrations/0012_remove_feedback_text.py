# Generated by Django 4.2 on 2024-11-05 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0011_alter_feedbackfile_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feedback",
            name="text",
        ),
    ]
