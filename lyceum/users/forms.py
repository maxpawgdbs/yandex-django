import django.contrib
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
import django.forms

import users.models


class ProfileForm(django.forms.ModelForm):
    class Meta:
        model = users.models.Profile
        fields = (
            "birthday",
            "image",
        )
        widgets = {
            "birthday": django.forms.DateInput(attrs={"date": True}),
        }
        exclude = ("coffee_count",)


class CustomUserForm(UserCreationForm):
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
    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            "first_name",
            "email",
        )


__all__ = ()
