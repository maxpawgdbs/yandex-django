import django.contrib
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

import users.models


class ProfileInline(django.contrib.admin.TabularInline):
    model = users.models.Profile

    can_delete = False


# временая моделька для отладки
@django.contrib.admin.register(users.models.Profile)
class FeedbackAdmin(django.contrib.admin.ModelAdmin):
    fields = ("coffee_count", "user")


class ProfileUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )
    list_editable = (
        "is_active",
        "is_staff",
    )


django.contrib.admin.site.unregister(User)
django.contrib.admin.site.register(User, ProfileUserAdmin)

__all__ = ()
