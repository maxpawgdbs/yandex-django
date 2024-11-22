__all__ = ()
import django.forms

from feedback.models import Feedback, FeedbackFile, FeedbackText


class FeedbackForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Feedback
        fields = (
            Feedback.name.field.name,
            Feedback.mail.field.name,
        )
        exclude = (
            Feedback.created_on.field.name,
            Feedback.status.field.name,
        )
        labels = {
            Feedback.name.field.name: "Имя",
            Feedback.mail.field.name: "Email",
        }
        help_texts = {
            Feedback.name.field.name: "Имя",
            Feedback.mail.field.name: "Email",
        }
        widgets = {
            Feedback.name.field.name: django.forms.TextInput(
                attrs={"class": "form-control"},
            ),
            Feedback.mail.field.name: django.forms.EmailInput(
                attrs={"type": "email", "class": "form-control"},
            ),
        }
        email = {
            "required": True,
        }


class FeedbackTextForm(django.forms.ModelForm):
    class Meta:
        model = FeedbackText
        fields = (FeedbackText.text.field.name,)
        labels = {FeedbackText.text.field.name: "Текст"}
        help_texts = {FeedbackText.text.field.name: "Текст"}
        widgets = {
            FeedbackText.text.field.name: django.forms.TextInput(
                attrs={"class": "form-control"},
            ),
        }


class FeedbackFilesForm(django.forms.ModelForm):
    class Meta:
        model = FeedbackFile
        fields = (FeedbackFile.file.field.name,)
        labels = {FeedbackFile.file.field.name: "Файлы"}
        help_texts = {FeedbackFile.file.field.name: "Файлы"}
        widgets = {
            FeedbackFile.file.field.name: django.forms.FileInput(
                attrs={"multiple": True, "class": "form-control"},
            ),
        }
