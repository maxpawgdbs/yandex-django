# Generated by Django 4.2 on 2024-11-22 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0017_feedback_text"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feedback",
            name="text",
        ),
    ]