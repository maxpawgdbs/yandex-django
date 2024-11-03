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
                subject=form.cleaned_data["name"],
                message=form.cleaned_data["text"],
                from_email=django.conf.settings.EMAIL_HOST,
                recipient_list=[
                    form.cleaned_data["mail"],
                ],
            )
            django.contrib.messages.success(
                request,
                "Фидбек принят 👌",
            )
            return django.shortcuts.redirect("feedback:feedback")
    else:
        form = feedback_forms.FeedbackForm()

    template = "feedback/feedback.html"
    context = {"form": form}
    return django.shortcuts.render(request, template, context)


__all__ = ()
