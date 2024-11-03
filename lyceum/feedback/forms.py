import django.forms

import feedback.models


class FeedbackForm(django.forms.ModelForm):
    class Meta:
        model = feedback.models.Feedback
        fields = (
            "text",
            "mail",
        )
        exclude = ("created_on", "name")
        labels = {
            "text": "Фидбек",
            "mail": "Email",
        }
        help_texts = {
            "text": "Фидбек",
            "mail": "Email",
        }
        widgets = {
            "text": django.forms.TextInput(attrs={"class": "form-control"}),
            "mail": django.forms.EmailInput(
                attrs={"type": "email", "class": "form-control"},
            ),
        }
        email = {
            "required": True,
        }


__all__ = ()
