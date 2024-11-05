import django.conf
import django.contrib.messages
import django.core.mail
import django.shortcuts

import feedback.forms as feedback_forms
import feedback.models as feedback_models


def feedback(request):
    if request.method == "POST":
        form = feedback_forms.FeedbackForm(request.POST or None)
        if form.is_valid():
            form.save()
            last = feedback_models.Feedback.objects.all()[::-1][0]
            files = request.FILES.getlist("files")
            for file in files:
                f = feedback_models.FeedbackFile(
                    feedback=last,
                    file=file,
                )
                f.full_clean()
                f.save()

            name = form.cleaned_data["name"]
            text = form.cleaned_data["text"]
            mail = form.cleaned_data["mail"]
            result = django.core.mail.send_mail(
                subject=name,
                message=text,
                from_email=django.conf.settings.DJANGO_MAIL,
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
