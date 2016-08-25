from django import forms
from django.forms.models import modelformset_factory

from .models import video

class ProductFilterForm(forms.Form):
    q = forms.CharField(label='search', required=False)
    video_id = forms.ModelMultipleChoiceField(
        label='video',
        queryset=video.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)



