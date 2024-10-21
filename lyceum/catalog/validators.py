import re

import django.core.exceptions
import django.core.validators


class ValidateMustContain:
    def __init__(self, *params):
        self.params = params

    def __call__(self, value):
        text = value.lower().split()
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


def custom_validator_zero(value):
    if value <= 0 or value > 32767:
        raise django.core.exceptions.ValidationError(
            "Вес не соотвествует стандартам",
        )


__all__ = [
    ValidateMustContain,
    custom_validator_zero,
]
