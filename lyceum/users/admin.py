import django.contrib
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

import users.models


class ProfileInline(django.contrib.admin.TabularInline):
    model = users.models.Profile

    can_delete = False

    readonly_fields = (
        users.models.Profile.coffee_count.field.name,
        users.models.Profile.birthday.field.name,
    )


# временая моделька для отладки
@django.contrib.admin.register(users.models.Profile)
class FeedbackAdmin(django.contrib.admin.ModelAdmin):
    fields = (
        users.models.Profile.coffee_count.field.name,
        users.models.Profile.user.field.name,
    )


class ProfileUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        User.username.field.name,
        User.email.field.name,
        User.first_name.field.name,
        User.last_name.field.name,
        User.is_active.field.name,
        User.is_staff.field.name,
    )
    list_editable = (
        User.is_active.field.name,
        User.is_staff.field.name,
    )
    readonly_fields = (User.email.field.name,)


django.contrib.admin.site.unregister(User)
django.contrib.admin.site.register(User, ProfileUserAdmin)

__all__ = ()
