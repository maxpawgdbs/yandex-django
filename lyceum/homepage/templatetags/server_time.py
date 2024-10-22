import datetime
import time

from django import template

register = template.Library()


@register.simple_tag
def time_from_server():
    return str(time.time())


@register.simple_tag
def year_from_server():
    return datetime.datetime.now().strftime("%Y")


__all__ = [
    time_from_server,
    year_from_server,
]
