import django.conf
import django.core
import django.db.models


# еще одна функция
# которая уже часть корабля
def get_upload_to(instance, filename):
    return f"uploads/{instance.feedback.id}/{filename}"


class Feedback(django.db.models.Model):
    name = django.db.models.CharField(
        null=False,
        verbose_name="Имя пользователя",
        max_length=150,
        blank=True,
    )
    created_on = django.db.models.DateTimeField(auto_now_add=True)
    mail = django.db.models.EmailField(
        null=False,
        verbose_name="Почта пользователя",
    )
    status = django.db.models.CharField(
        max_length=8,
        choices=(
            ("NEW", "получено"),
            ("PENDING", "в обработке"),
            ("COMPLETE", "ответ дан"),
        ),
        default="NEW",
    )


class FeedbackText(django.db.models.Model):
    feedback = django.db.models.OneToOneField(
        Feedback,
        on_delete=django.db.models.CASCADE,
    )
    text = django.db.models.TextField(
        null=False,
        verbose_name="Жалоба",
    )

    def delete(self, *args, **kwargs):
        if self.feedback is not None:
            raise django.core.exceptions.ValidationError("НЕЛЬЗЯ!!!")

        super().delete(*args, **kwargs)


class FeedbackFile(django.db.models.Model):
    def get_upload_path(self, filename):
        return f"uploads/{self.feedback.id}/{filename}"

    feedback = django.db.models.ForeignKey(
        Feedback,
        on_delete=django.db.models.CASCADE,
    )
    file = django.db.models.FileField(
        upload_to=get_upload_path,
        null=True,
        blank=True,
    )


class StatusLog(django.db.models.Model):
    user = django.db.models.ForeignKey(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        null=True,
    )
    timestamp = django.db.models.DateTimeField(auto_now_add=True)
    from_status = django.db.models.CharField(
        max_length=8,
        db_column="from",
        null=False,
    )
    to = django.db.models.CharField(
        max_length=8,
        db_column="to",
        null=False,
    )


__all__ = ()
