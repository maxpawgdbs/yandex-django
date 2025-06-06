__all__ = ()

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
import django.forms

import users.models


class ProfileForm(django.forms.ModelForm):
    class Meta:
        model = users.models.Profile
        fields = (
            users.models.Profile.birthday.field.name,
            users.models.Profile.image.field.name,
            users.models.Profile.coffee_count.field.name,
        )
        widgets = {
            users.models.Profile.birthday.field.name: django.forms.DateInput(
                attrs={"date": True},
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["coffee_count"].widget.attrs["disabled"] = True


class CustomUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


class CustomChangeUserForm(UserChangeForm):
    password = None

    def __init__(self, *args, **kwargs):
        super(CustomChangeUserForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["disabled"] = True

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            "first_name",
            "email",
        )
        exclude = ("password",)
