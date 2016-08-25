import django_filters
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, Http404
from django_filters import FilterSet, CharFilter, NumberFilter



# Create your views here.

from .forms import ProductFilterForm
from .models import video, Category

#@login_required    
def video_detail(request, cat_slug, id):        
    try:
        cat = Category.objects.get(slug=cat_slug)                
    except:
        raise Http404
    try:
        obj = video.objects.get(id=id)
        print (obj)        
        return render(request, "video_details.html", {"obj":obj})
    except:
        raise Http404

def category_list(request):
    queryset = Category.objects.all()    
    
    
    context = {
        "queryset": queryset,
    }
    return render(request, "category_list.html", context)

#@login_required

def category_detail(request, cat_slug):    
    obj = Category.objects.get(slug=cat_slug)    
    queryset = obj.video_set.all()
    #query_list = Category.objects.active()
    #query_list = video.objects.all()
    #query = request.GET.get("q")
    #if query:
    #    query_set = query_list.filter(title__icontains=query)
    #else:
    #    raise Error
    return render(request, "video_list.html", {"obj":obj, "queryset": queryset})
            
class ProductFilter(django_filters.FilterSet):
	title = CharFilter(name='title', lookup_type='icontains', distinct=True)
class Meta:
	model = video
	fields = [
	'title',
	]

