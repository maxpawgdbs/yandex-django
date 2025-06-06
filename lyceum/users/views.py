__all__ = ()

from django.conf import settings
import django.contrib
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import django.core
import django.shortcuts
import django.urls
import django.utils

import users.forms
import users.models


def signup(request):
    if request.method == "POST":
        form = users.forms.CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            normalized_email = users.models.ProxyUser.objects.normalize_email(
                email,
            )
            password = form.cleaned_data["password1"]
            last = User.objects.create_user(
                username,
                normalized_email,
                password,
            )
            last.is_active = settings.DEFAULT_USER_IS_ACTIVE
            last.save()
            if not settings.DEFAULT_USER_IS_ACTIVE:
                mail_url = django.urls.reverse(
                    "users:activate",
                    args=[last.username],
                )
                url = f"{request.scheme}://{request.get_host()}{mail_url}"
                result = django.core.mail.send_mail(
                    subject=last.username,
                    message="У вас 12 часов на активацию "
                    "профиля на нашем сайте\n"
                    f"вот ссылка: {url}",
                    from_email=settings.DJANGO_MAIL,
                    recipient_list=[
                        last.email,
                    ],
                    fail_silently=False,
                )

                if result:
                    message = "Отправили письмо активации на почту"
                else:
                    message = "Ну вы где-то начудили"

                django.contrib.messages.success(
                    request,
                    message,
                )

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    django.contrib.messages.error(request, f"{field}: {error}")

        return django.shortcuts.redirect("users:signup")

    form = users.forms.CustomUserForm()
    context = {"form": form}
    return django.shortcuts.render(request, "users/signup.html", context)


def activate(request, username):
    obj = django.shortcuts.get_object_or_404(
        User.objects,
        username=username,
    )
    date = obj.date_joined
    hours = django.utils.timezone.now() - date
    hours = hours.total_seconds() / 3600
    if obj.profile.attempts_count >= django.conf.settings.MAX_AUTH_ATTEMPTS:
        if hours < 24 * 7:
            obj.is_active = True
            obj.save()
    else:
        if hours < 12:
            obj.is_active = True
            obj.save()

    return django.shortcuts.render(request, "users/activate.html")


@login_required
def profile(request):
    if request.method == "POST":
        userform = users.forms.CustomChangeUserForm(request.POST or None)
        profileform = users.forms.ProfileForm(request.POST or None)
        if profileform.is_valid() and userform.is_valid():
            name = userform.cleaned_data["first_name"]
            birthday = profileform.cleaned_data["birthday"]
            image = request.FILES.get("image")
            user = request.user

            if name:
                user.first_name = name

            user.full_clean()
            user.save()

            user_profile = request.user.profile

            if birthday:
                user_profile.birthday = birthday

            if request.POST.get("image-clear", False):
                user_profile.image.delete(save=False)

            if image:
                user_profile.image = image

            user_profile.full_clean()
            user_profile.save()

    userform = users.forms.CustomChangeUserForm(instance=request.user)
    profileform = users.forms.ProfileForm(instance=request.user.profile)
    context = {
        "image": request.user.profile.image,
        "form": profileform,
        "userform": userform,
    }
    return django.shortcuts.render(request, "users/profile.html", context)


def user_detail(request, pk):
    user = django.shortcuts.get_object_or_404(
        User,
        id=pk,
    )
    context = {
        "profile": user,
    }
    return django.shortcuts.render(request, "users/user_detail.html", context)


def user_list(request):
    users = User.objects.filter(is_active=True)
    context = {
        "users": users,
    }
    return django.shortcuts.render(request, "users/user_list.html", context)
