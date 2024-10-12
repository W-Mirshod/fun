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


@register.filter
def wrap_text(value, length=25):
    """
    Breaks text into lines with a maximum length of `length` characters.
    """
    words = [value[i:i + length] for i in range(0, len(value), length)]
    return '-\n'.join(words)
