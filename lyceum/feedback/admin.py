import django.contrib

import feedback.models


@django.contrib.admin.register(feedback.models.Feedback)
class FeedbackAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        feedback.models.Feedback.name.field.name,
        feedback.models.Feedback.text.field.name,
        feedback.models.Feedback.created_on.field.name,
        feedback.models.Feedback.mail.field.name,
    )
    fields = (
        feedback.models.Feedback.name.field.name,
        feedback.models.Feedback.text.field.name,
        feedback.models.Feedback.created_on.field.name,
        feedback.models.Feedback.mail.field.name,
    )


__all__ = ()
