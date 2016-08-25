from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
#from einsteinish.utils import unique_slugify
from django.template.defaultfilters import slugify

class Resource(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    created_by = models.ForeignKey(User, related_name='provider', null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    video_upload = models.FileField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'pk': self.id})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = '%s' %self.title
            #unique_slugify(self, slug_str)
        super(Resource, self).save(*args, **kwargs)
            
