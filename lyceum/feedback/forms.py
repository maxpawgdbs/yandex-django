import django.forms

import feedback.models


class FeedbackForm(django.forms.ModelForm):
    class Meta:
        model = feedback.models.Feedback
        fields = (
            "name",
            "text",
            "mail",
        )
        exclude = ("created_on",)
        labels = {
            "name": "Имя",
            "text": "Фидбек",
            "mail": "Email",
        }
        help_texts = {
            "name": "Имя",
            "text": "Фидбек",
            "mail": "Email",
        }
        widgets = {
            "name": django.forms.TextInput(attrs={"class": "form-control"}),
            "text": django.forms.TextInput(attrs={"class": "form-control"}),
            "mail": django.forms.EmailInput(
                attrs={"type": "email", "class": "form-control"},
            ),
        }


__all__ = ()
