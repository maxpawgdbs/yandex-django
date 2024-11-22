__all__ = ()
import re

import django.core.exceptions
import django.core.validators
from django.utils.html import strip_tags


class ValidateMustContain:
    def __init__(self, *params):
        self.params = params

    def __call__(self, value):
        text_without_tags = strip_tags(value)
        text = text_without_tags.lower().split()
        for w in text:
            w = re.sub(r"^\W+|\W+$", "", w)
            if w in self.params:
                return

        raise django.core.exceptions.ValidationError(
            "текст должен содержать {}".format(value),
        )

    def deconstruct(self):
        return (
            "catalog.validators.ValidateMustContain",
            self.params,
            {},
        )


# Функцию уже не изменить. Она уже часть корабля.
# При миграции происходит это:
# 1) validators=[catalog.validators.custom_validator_zero],
# 2)             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# 3) AttributeError: module 'catalog.validators'
# 3) has no attribute 'custom_validator_zero'
def custom_validator_zero(value):
    if value <= 0 or value > 32767:
        raise django.core.exceptions.ValidationError(
            "Вес не соотвествует стандартам",
        )
