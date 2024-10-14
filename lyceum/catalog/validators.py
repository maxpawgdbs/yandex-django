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
        raise django.core.exceptions.ValidationError("error")

    def deconstruct(self):
        return (
            "catalog.validators.ValidateMustContain",
            self.params,
            {},
        )


def custom_validator_zero(value):
    if value <= 0 or value > 32767:
        raise django.core.exceptions.ValidationError("error")


def normalizaciya(word):
    cap_chars = {
        "T": "Т",
        "B": "В",
        "M": "М",
        "H": "Н",
    }
    low_chars = {
        "a": "а",
        "c": "с",
        "e": "е",
        "o": "о",
        "p": "р",
        "x": "х",
    }
    word = re.sub(r"[^\w\s]", "", word)
    word = " ".join(word.split())
    for i in cap_chars:
        word = word.replace(i, cap_chars[i])
    for i in low_chars:
        word = word.replace(i, low_chars[i])
    word = word.lower()
    return word
