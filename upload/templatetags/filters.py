
from django.core.urlresolvers import reverse
from django import template

from myaccount.models import SavedResource

register = template.Library()


@register.filter
def issaved(resource, user):
    try:
        SavedResource.objects.get(resource=resource, user=user)
        return True
    except SavedResource.DoesNotExist:
        return False