"""vidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from vidos import views
from upload.views import ResourceCreateView, ResourceDetailView, ResourceSaveView, ResourceUpdateView, ResourceAllListView
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView



urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^staff/$', views.staff_home, name='staff'),
    url(r'^logout/$', views.auth_logout, name='logout'),
    url(r'^login/$', views.auth_login, name='login'),
    url(r'^register/$', views.user_register, name='register'),
    #url(r'', include('webmaster_verification.urls')),
    #url(r'^profile/$', MyProfileView.as_view(), name='profile'),
    #url(r'^update/$', UserUpdateView.as_view(), name='update'),
    url(r'^lists/$', 'myaccount.views.list', name='lists'),
    url(r'^delete/$', 'myaccount.views.Document_delete', name='delete'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^(?P<pk>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^(?P<pk>\d+)/save/$', ResourceSaveView.as_view(), name='resource_save'),
    url(r'^(?P<pk>\d+)/edit/$', ResourceUpdateView.as_view(), name='resource_update'),
    url(r'^news/$', 'upload.views.ResourceAllListView', name='resource_list'),
    #url(r'^new/$', login_required(ResourceCreateView.as_view(template_name="resource_detail.html"), name='resource_create')),
    url(r'^new/$',ResourceCreateView.as_view(), name='resource_create'),
    
    
    
    
    url(r'^videos/$', 'videos.views.category_list', name='category_list'),
    
    
    url(r'^videos/(?P<cat_slug>[\w-]+)/$', 'videos.views.category_detail', name='category_detail'),
    url(r'^videos/(?P<cat_slug>[\w-]+)/(?P<id>\d+)/$', 'videos.views.video_detail', name='video_detail'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    
    #url(r'^$', views.list, name='list'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



