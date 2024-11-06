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

    def delete(self, *args, **kwargs):
        raise django.core.exceptions.PermissionDenied(
            "Удаление объектов этого типа запрещено.",
        )

    def has_delete_permission(self, request, obj=None):
        return False


class FeedbackText(django.db.models.Model):
    feedback = django.db.models.OneToOneField(
        Feedback,
        on_delete=django.db.models.PROTECT,
    )
    text = django.db.models.TextField(
        null=False,
        verbose_name="Жалоба",
    )


class FeedbackFile(django.db.models.Model):
    feedback = django.db.models.ForeignKey(
        Feedback,
        on_delete=django.db.models.PROTECT,
    )

    def get_upload_path(self, filename):
        return f"uploads/{self.feedback_id}/{filename}"

    def upload_to(self, filename):
        return self.get_upload_path(filename)

    file = django.db.models.FileField(
        upload_to=upload_to,
        null=True,
        blank=True,
    )


class StatusLog(django.db.models.Model):
    user = django.db.models.ForeignKey(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.PROTECT,
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


def delete_feedback(sender, instance, **kwargs):
    instance.feedback.delete()


django.db.models.signals.post_delete.connect(delete_feedback, sender=Feedback)

__all__ = ()
