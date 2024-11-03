import django.forms


class EchoForm(django.forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    text = django.forms.CharField(
        label="Эхо",
        help_text="Эхо",
    )

__all__ = ()
