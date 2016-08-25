#import urllib

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.


    


class VideoQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    def featured(self):
        return self.filter(featured=True)
    

class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)
    
    def get_featured(self):
        return self.get_queryset().active().featured()
    
    def all(self):
        return self.get_queryset().active()
    
DEFAULT_MESSAGE = "Check out this awsome video"
    
class video(models.Model):
    title = models.CharField(max_length=120)
    embed_code = models.CharField(max_length=500, null=True, blank=True)
    share_message = models.TextField(default="DEFAULT_MESSAGE")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    product_img = models.CharField(max_length=500, null=True, blank=True)
    product_embed = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    free_preview = models.BooleanField(default=False)
    category = models.ForeignKey("Category", default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    
    
    objects = VideoManager()
    #code
    
    class Meta:
        unique_together = ('slug', 'category')
        
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
            return reverse("video_detail", kwargs={"id": self.id, "cat_slug": self.category.slug})
        
    def get_share_link(self):
        full_url = "%s%s" %(settings.FULL_DOMAIN_NAME, self.get_absolute_url())
        return full_url
                         
    def get_share_message(self):
        full_url = "%s%s" %(settings.FULL_DOMAIN_NAME, self.get_absolute_url())
        return (self.share_message, full_url)
    def get_image_url(self):
        return "%s%s" %(settings.MEDIA_URL, self.image)
        
        
        
    #def video_post_save_receiver(sender, instatnce, created,  *args, **kwargs):
        #print ("signal sent")
        #if created:
            #slug_title = slugify(instance.title)
            #new_slug = "%s %s %s" %(instance.title, instance.category.slug, instance.id)
            #try:
                #obj_exists = video.objects.get(slug=slug_title, category=instance.category)
                #instance.slug = slugify(new_slug)
                #instance.save()
                #print ("model exists, new slug generated")
            #except video.DoesNotExist:
                #instance.slug = slug_title
                #instance.save()
                #print ("slug and model created")
            #except video.MultipleObjectsReturned:
                #instance.slug = slugify(new_slug)
                #instance.save()
                #print ("multiple models exist, new slug generated")
            #except:
                #pass
        
        
    #post_save.connect(video_post_save_receiver, sender=video)

        

class CategoryQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True)


class CategoryManager(models.Manager):
	def get_queryset(self):
		return CategoryQuerySet(self.model, using=self._db)

	def get_featured(self):
		#Video.objects.get_featured(user, kabc="something")
		#Video.objects.filter(featured=True)
		#return super(VideoManager, self).filter(featured=True)
		return self.get_queryset().active().featured()

	def all(self):
		return self.get_queryset().active()

class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    slug = models.SlugField(default='abc', unique=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    objects = CategoryManager()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"cat_slug": self.slug})
        
    def get_image_url(self):
        return "%s%s" %(settings.MEDIA_URL, self.image)
        
    
       

   

    