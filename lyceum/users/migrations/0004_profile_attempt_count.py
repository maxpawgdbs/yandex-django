# Generated by Django 4.2 on 2024-11-15 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_proxyuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="attempt_count",
            field=models.IntegerField(default=0),
        ),
    ]
