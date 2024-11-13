from django.conf import settings
import django.contrib
from django.contrib.auth.models import User
import django.core
import django.shortcuts
import django.utils

import users.forms


def signup(request):
    if request.method == "POST":
        form = users.forms.CustomUserForm(request.POST)
        profileform = users.forms.ProfileForm(request.POST)
        if form.is_valid() and profileform.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            last = User.objects.create_user(
                username,
                email,
                password,
            )
            profile = users.models.Profile(
                user=last,
            )
            birthday = profileform.cleaned_data["birthday"]
            image = request.FILES.get("image")

            if birthday:
                profile.birthday = birthday

            if image:
                profile.image = image

            profile.full_clean()
            profile.save()
            result = django.core.mail.send_mail(
                subject=last.username,
                message="У вас 12 часов на активацию профиля на нашем сайте\n"
                f"вот ссылка: 127.0.0.1/users/activate/{last.username}",
                from_email=settings.DJANGO_MAIL,
                recipient_list=[
                    last.email,
                ],
                fail_silently=False,
            )

            if result:
                django.contrib.messages.success(
                    request,
                    "Отправили письмо активации на почту",
                )

            else:
                django.contrib.messages.success(
                    request,
                    "Ну вы где-то начудили",
                )

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    django.contrib.messages.error(request, f"{field}: {error}")

        return django.shortcuts.redirect("users:signup")

    form = users.forms.CustomUserForm()
    profileform = users.forms.ProfileForm()
    context = {"form": form, "profileform": profileform}
    return django.shortcuts.render(request, "users/registration.html", context)


def activate(request, username):
    obj = django.shortcuts.get_object_or_404(
        User.objects,
        username=username,
    )
    date = obj.date_joined
    hours = django.utils.timezone.now() - date
    hours = hours.total_seconds() / 3600

    if hours > 12:
        obj.is_active = True
        obj.save()

    return django.shortcuts.render(request, "users/activate.html")


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profileform = users.forms.ProfileForm(request.POST or None)
            if profileform.is_valid():
                name = request.POST.get("name")
                email = request.POST.get("email")
                birthday = profileform.cleaned_data["birthday"]
                image = request.FILES.get("image")
                user = request.user
                print(name, user)

                if name:
                    user.first_name = name

                if email:
                    user.email = email

                user.full_clean()
                user.save()
                user_profile = request.user.profile

                if birthday:
                    user_profile.birthday = birthday

                if image:
                    user_profile.image = image

                user_profile.full_clean()
                user_profile.save()

        profileform = users.forms.ProfileForm(instance=request.user.profile)
        context = {"profile": request.user, "form": profileform}
        return django.shortcuts.render(request, "users/profile.html", context)

    return django.shortcuts.redirect("users:login")


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


__all__ = ()
