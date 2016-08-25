from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
#from django.template.defaultfilters import slugify
from django.utils.text import slugify
from upload.models import Resource




class MyUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
        	raise ValueError('Must include username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
            
        user.set_password(password)
        user.save()
        #user.save(using=self._db)
        return user

    def create_superuser(self, username, email,  password):
        """
        Creates and saves a superuser with the given username, email and password.
        """

        user = self.create_user(
            username = username,
            email = email,
            password = password,
        )
        user.is_admin = True
        #user.save(using=self._db)
        user.save()
        return user


class MyUser(AbstractBaseUser):
	username = models.CharField(
	    max_length=255,
	    unique=True,
	)
	email = models.EmailField(
	    verbose_name='email address',
	    max_length=255,
	    unique=True,
	)
	first_name = models.CharField(
			max_length=120,
			null=True,
			blank=True,
			)
	last_name = models.CharField(
			max_length=120,
			null=True,
			blank=True,
			)
	is_member = models.BooleanField(default=False, 
					verbose_name='Is Paid Member')
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_full_name(self):
	    # The user is identified by their email address
	    return "%s %s" %(self.first_name, self.last_name)

	def get_short_name(self):
	    # The user is identified by their email address
	    return self.first_name

	def __str__(self):
	    return self.username

	#def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    # Simplest possible answer: Yes, always
	    #return True

	#def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    # Simplest possible answer: Yes, always
	    #return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_admin







#class UserProfile(models.Model):
#	user = models.OneToOneField(MyUser)
#	bio = models.TextField(null=True, blank=True)
#	facebook_link = models.CharField(max_length=320, 
#		null=True, 
#		blank=True, 
#		verbose_name='Facebook profile url')
#	twitter_handle = models.CharField(max_length=320, 
#		null=True, 
#		verbose_name='Twitter handle')		


#	def __str__(self):
#		return self.user.email


class UserProfile(models.Model):
    user = models.OneToOneField(MyUser)
    
    def __str__(self):
        return self.user.email
    
    
class Document(models.Model):
    #user = models.OneToOneField(User)
    title = models.CharField(max_length=255, unique=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, default='')
    #url = models.URLField(unique=True, null=True)
    #created_by = models.ForeignKey(User, null=True)
    #created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    #updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)
    #show = models.BooleanField(default=True)
    #thumbnail = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True)
    docfile = models.FileField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    
    #def __str__(self):
    #    return self.title
    
    
    def get_absolute_url(self):
        return reverse("list", kwargs={"user_slug": self.slug})
    
    
class SavedResource(models.Model):
    user = models.ForeignKey(User)
    resource = models.ForeignKey(Resource)
    saved_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = (('user', 'resource'),)

    def __str__(self):
        return '%s %s' %(self.user, self.resource)
    
    
    
    
    
    
        
    
    
    
    



