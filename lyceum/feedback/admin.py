__all__ = ()
import django.contrib

import feedback.models


class TextInline(django.contrib.admin.TabularInline):
    model = feedback.models.FeedbackText
    extra = 1
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@django.contrib.admin.register(feedback.models.Feedback)
class FeedbackAdmin(django.contrib.admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            statuslog = feedback.models.StatusLog(
                user=request.user,
                from_status=feedback.models.Feedback.objects.get(
                    pk=obj.id,
                ).status,
                to=obj.status,
            )
            statuslog.full_clean()
            statuslog.save()

        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = (
        feedback.models.Feedback.name.field.name,
        feedback.models.Feedback.mail.field.name,
        feedback.models.Feedback.created_on.field.name,
        feedback.models.Feedback.status.field.name,
    )
    fields = (
        feedback.models.Feedback.name.field.name,
        feedback.models.Feedback.mail.field.name,
        feedback.models.Feedback.status.field.name,
    )
    readonly_fields = (
        feedback.models.Feedback.name.field.name,
        feedback.models.Feedback.mail.field.name,
        feedback.models.Feedback.created_on.field.name,
        TextInline,
    )
    list_editable = (feedback.models.Feedback.status.field.name,)
    inlines = [
        TextInline,
    ]


@django.contrib.admin.register(feedback.models.StatusLog)
class StatusLogAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        feedback.models.StatusLog.user.field.name,
        feedback.models.StatusLog.timestamp.field.name,
        feedback.models.StatusLog.from_status.field.name,
        feedback.models.StatusLog.to.field.name,
    )
    readonly_fields = (
        feedback.models.StatusLog.user.field.name,
        feedback.models.StatusLog.timestamp.field.name,
        feedback.models.StatusLog.from_status.field.name,
        feedback.models.StatusLog.to.field.name,
    )
