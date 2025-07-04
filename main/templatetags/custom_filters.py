from django import template

register = template.Library()

@register.filter
def make_groups_of(value, n):
    n = int(n)
    return [value[i:i + n] for i in range(0, len(value), n)]
