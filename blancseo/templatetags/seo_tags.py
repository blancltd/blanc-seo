from django import template
from django.contrib.contenttypes.models import ContentType

from ..models import MetaContent

register = template.Library()


@register.inclusion_tag('seo.html', takes_context=True)
def seo(context, obj=None, title=None):
    # Fall back to getting object from context for convenience
    if obj is None:
        obj = context.get('object', obj)

    meta = None

    # If we're given an object, try and find the relevant MetaContent for it
    if obj:
        content_type = ContentType.objects.get_for_model(obj)

        try:
            meta = MetaContent.objects.get(content_type=content_type, object_id=obj.pk)
        except MetaContent.DoesNotExist:
            pass

    # No object, so we'll use the URLMetaContent provided in the template context
    elif obj is None:
        meta = context.get('url_metacontent')

    return {
        'object': obj,
        'title': title,
        'meta': meta,
    }
