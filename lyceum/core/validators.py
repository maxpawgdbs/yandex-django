import re

import django.core.exceptions


def custom_validator_spaces(value):
    if len(value.split()) == 0:
        raise django.core.exceptions.ValidationError("имя из пробелов")


def normalization(word):
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
        "k": "к",
    }
    word = re.sub(r"[^\w\s]", "", word)
    word = " ".join(word.split())
    for i in cap_chars:
        word = word.replace(i, cap_chars[i])
    word = word.lower()
    for i in low_chars:
        word = word.replace(i, low_chars[i])
    return word
