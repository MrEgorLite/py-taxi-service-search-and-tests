from typing import LiteralString

from django import template
from django.http import HttpRequest

register = template.Library()

@register.simple_tag
def query_transform(request: HttpRequest, **kwargs) -> LiteralString:
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, None)
    return updated.urlencode()