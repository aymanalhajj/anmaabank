from django import template
from django.template.defaultfilters import stringfilter
from django.utils.translation import (
    gettext_lazy,
    ngettext,
    ngettext_lazy,
    npgettext_lazy,
    pgettext,
    round_away_from_one,
)
from django.template import defaultfilters

register = template.Library()
# Create your views here.


@register.filter
def to_and(value):

    return value.split(' ')[0]


register = template.Library()


@register.filter
def to_str(value):
    """converts int to string"""
    return str(value)


@register.filter
def to_lat(value):
    """converts int to string"""
    return str(value).replace(',', '.')
# class to_and:
#     register = template.Library()

#     @register.filter
#     def to_and(value):
#         return value.replace(" ", "-")


@register.filter
def in_column_navbar_chield(things, child):
    return things.filter(column_navbar_chield__in=child)


@register.filter
def in_type_services(things, type):
    return things.filter(type_services=type)


@register.filter
def in_categories_services(things, categories_services):
    return things.filter(category_services=categories_services.id)


@register.filter
def check_share_url(value):

    if str(value).endswith('.net') or str(value).endswith('net/') or str(value).endswith('.com') or str(value).endswith('com/') or value.endswith('7847') or str(value).endswith("7847/") or value.endswith('7676') or str(value).endswith("7676/"):
        return False
    else:
        return True


# A tuple of standard large number to their converters
intword_converters = (
    (3, lambda number: ngettext("%(value)s الف", "%(value)s الف", number)),
    # (4, lambda number: ngettext("%(value)s عشرة", "%(value)s الف", number)),

    (6, lambda number: ngettext("%(value)s million", "%(value)s million", number)),
    (9, lambda number: ngettext("%(value)s billion", "%(value)s billion", number)),
    (12, lambda number: ngettext("%(value)s trillion", "%(value)s trillion", number)),
    (
        15,
        lambda number: ngettext(
            "%(value)s quadrillion", "%(value)s quadrillion", number
        ),
    ),
    (
        18,
        lambda number: ngettext(
            "%(value)s quintillion", "%(value)s quintillion", number
        ),
    ),
    (
        21,
        lambda number: ngettext("%(value)s sextillion",
                                "%(value)s sextillion", number),
    ),
    (
        24,
        lambda number: ngettext("%(value)s septillion",
                                "%(value)s septillion", number),
    ),
    (27, lambda number: ngettext("%(value)s octillion", "%(value)s octillion", number)),
    (30, lambda number: ngettext("%(value)s nonillion", "%(value)s nonillion", number)),
    (33, lambda number: ngettext("%(value)s decillion", "%(value)s decillion", number)),
    (100, lambda number: ngettext("%(value)s googol", "%(value)s googol", number)),
)


@register.filter
def intToword(value):
    """
    Convert a large integer to a friendly text representation. Works best
    for numbers over 1 million. For example, 1000000 becomes '1.0 million',
    1200000 becomes '1.2 million' and '1200000000' becomes '1.2 billion'.
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value

    abs_value = abs(value)
    if abs_value < 1000:
        return value

    for exponent, converter in intword_converters:
        large_number = 10**exponent
        if abs_value < large_number * 1000:
            new_value = value / large_number
            rounded_value = round_away_from_one(new_value)
            return converter(abs(rounded_value)) % {
                "value": defaultfilters.floatformat(new_value, 0),
            }
    return value
