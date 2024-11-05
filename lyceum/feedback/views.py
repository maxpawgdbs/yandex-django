import django.conf
import django.contrib.messages
import django.core.mail
import django.shortcuts

import feedback.forms as feedback_forms
import feedback.models as feedback_models


def feedback(request):
    form = feedback_forms.FeedbackForm(request.POST or None)
    textform = feedback_forms.FeedbackTextForm(request.POST or None)
    fileform = feedback_forms.FeedbackFilesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            last = feedback_models.Feedback.objects.all()[::-1][0]
            name = form.cleaned_data["name"]
            mail = form.cleaned_data["mail"]
            if fileform.is_valid():
                files = request.FILES.getlist("file")
                for file in files:
                    f = feedback_models.FeedbackFile(
                        feedback=last,
                        file=file,
                    )
                    f.full_clean()
                    f.save()
                if textform.is_valid():
                    text = textform.cleaned_data["text"]
                    t = feedback_models.FeedbackText(
                        feedback=last,
                        text=text,
                    )
                    t.full_clean()
                    t.save()
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
        textform = feedback_forms.FeedbackTextForm()
        fileform = feedback_forms.FeedbackFilesForm()

    template = "feedback/feedback.html"
    context = {"form": form, "textform": textform, "fileform": fileform}
    return django.shortcuts.render(request, template, context)


__all__ = ()
