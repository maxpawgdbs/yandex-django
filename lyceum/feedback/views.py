import django.conf
import django.contrib.messages
import django.core.mail
import django.shortcuts

import feedback.forms as feedback_forms


def feedback(request):
    if request.method == "POST":
        form = feedback_forms.FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            django.core.mail.send_mail(
                "Фидбек принят 👌",
                form.cleaned_data.get("name"),
                django.conf.settings.DJANGO_MAIL,
                [
                    form.cleaned_data.get("mail"),
                ],
            )
            django.contrib.messages.add_message(
                request,
                25,
                "Фидбек принят 👌",
            )
            return django.shortcuts.redirect("feedback:feedback")
    else:
        form = feedback_forms.FeedbackForm()
    template = "feedback/feedback.html"
    context = {"form": form}
    return django.shortcuts.render(request, template, context)


__all__ = ()
