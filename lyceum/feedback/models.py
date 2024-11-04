import django.db.models


class Feedback(django.db.models.Model):
    name = django.db.models.CharField(
        null=False,
        verbose_name="Имя пользователя",
        max_length=150,
    )
    text = django.db.models.TextField(
        null=False,
        verbose_name="Жалоба",
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


__all__ = ()
