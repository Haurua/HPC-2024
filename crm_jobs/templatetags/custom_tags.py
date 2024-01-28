import decimal

from django import template
import datetime

register = template.Library()


@register.filter()
def if_none(var):
    if var:
        return str(var)
    else:
        return "n/a"


@register.filter()
def if_fee(var):
    if var:
        return "£" + str(var)
    else:
        return "n/a"
