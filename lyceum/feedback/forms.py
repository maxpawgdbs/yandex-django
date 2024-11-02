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
            "name": django.forms.TextInput(attrs={"class": "form-conrol"}),
            "text": django.forms.TextInput(attrs={"class": "form-conrol"}),
            "mail": django.forms.EmailInput(
                attrs={"type": "email", "class": "form-conrol"},
            ),
        }


__all__ = ()
