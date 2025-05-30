# Generated by Django 4.2 on 2024-11-23 20:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_alter_profile_block_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="block_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="profile",
            name="coffee_count",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
