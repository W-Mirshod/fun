from django import template

register = template.Library()


@register.filter
def ordinal(number):
    try:
        number = int(number)
    except (TypeError, ValueError):
        return number

    if 11 <= number % 100 <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')

    return f"{number}{suffix}"
