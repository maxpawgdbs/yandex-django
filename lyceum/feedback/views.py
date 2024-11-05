import django.conf
import django.contrib.messages
import django.core.mail
import django.shortcuts

import feedback.forms as feedback_forms


def feedback(request):
    if request.method == "POST":
        form = feedback_forms.FeedbackForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data["name"]
            text = form.cleaned_data["text"]
            mail = form.cleaned_data["mail"]
            result = django.core.mail.send_mail(
                subject=name,
                message=text,
                from_email=django.conf.settings.EMAIL_HOST,
                recipient_list=[
                    mail,
                ],
                fail_silently=False,
            )
            if result:
                django.contrib.messages.success(
                    request,
                    "Фидбек принят 👌",
                )
            else:
                django.contrib.messages.success(
                    request,
                    "Где-то ошибка🤨",
                )

            return django.shortcuts.redirect("feedback:feedback")
    else:
        form = feedback_forms.FeedbackForm()

    template = "feedback/feedback.html"
    context = {"form": form}
    return django.shortcuts.render(request, template, context)


__all__ = ()
