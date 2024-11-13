import django.forms

import feedback.models


class FeedbackForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = feedback.models.Feedback
        fields = (
            "name",
            "mail",
            "text",
        )
        exclude = (
            "created_on",
            "status",
        )
        labels = {
            "name": "Имя",
            "text": "Текст",
            "mail": "Email",
        }
        help_texts = {
            "name": "Имя",
            "text": "Текст",
            "mail": "Email",
        }
        widgets = {
            "name": django.forms.TextInput(attrs={"class": "form-control"}),
            "text": django.forms.TextInput(attrs={"class": "form-control"}),
            "mail": django.forms.EmailInput(
                attrs={"type": "email", "class": "form-control"},
            ),
        }
        email = {
            "required": True,
        }


class FeedbackTextForm(django.forms.ModelForm):
    class Meta:
        model = feedback.models.FeedbackText
        fields = ("text",)
        labels = {"text": "Текст"}
        help_texts = {"text": "Текст"}
        widgets = {
            "text": django.forms.TextInput(attrs={"class": "form-control"}),
        }


class FeedbackFilesForm(django.forms.ModelForm):
    class Meta:
        model = feedback.models.FeedbackFile
        fields = ("file",)
        labels = {"file": "Файлы"}
        help_texts = {"file": "Файлы"}
        widgets = {
            "file": django.forms.FileInput(
                attrs={"multiple": True, "class": "form-control"},
            ),
        }


__all__ = ()
