from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def highlight_search(text, query):
    result = text.replace(query, f"<span class='highlight'>{query}</span>")
    return mark_safe(result)


    