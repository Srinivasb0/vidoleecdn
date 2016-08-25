from django.forms import ModelForm

from .models import Resource


class ResourceCreateForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ('created_by', 'slug')

class ResourceUpdateForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ('created_by', 'slug')