import re

import django.core.exceptions
import django.core.validators


def custom_validator_words(*params):
    def my_validator(value):
        text = value.lower().split()
        for w in text:
            w = re.sub(r"^\W+|\W+$", "", w)
            if w in params:
                return
        raise django.core.exceptions.ValidationError("error")

    my_validator.deconstruct = lambda: (
        "catalog.validators.custom_validator_words",
        params,
        {},
    )
    return my_validator


def custom_validator_zero(value):
    if value <= 0 or value > 32767:
        raise django.core.exceptions.ValidationError("error")
