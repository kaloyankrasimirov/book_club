from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def stars(value):
    try:
        rating = int(value)
    except (TypeError, ValueError):
        return ""

    full_rating = max(rating, 0)

    star_svg = """
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="16"
    height="16"
    viewBox="0 0 24 24"
    style="vertical-align: -2px;"
    aria-hidden="true"
>
    <path
        fill="#FF6E6E"
        d="M12 2.5l2.94 5.96 6.56.95-4.75 4.63 1.12 6.54L12 17.5l-5.87 3.08 1.12-6.54L2.5 9.41l6.56-.95L12 2.5z"
    />
</svg>
                """

    return mark_safe(star_svg * full_rating)