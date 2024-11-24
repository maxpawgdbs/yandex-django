__all__ = ()
import django.conf
from django.db.models.signals import post_save
from django.dispatch import receiver

import users.models


@receiver(post_save, sender=django.conf.settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        users.models.Profile.objects.create(user=instance)
