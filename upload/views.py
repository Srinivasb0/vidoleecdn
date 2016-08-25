from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, RedirectView
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, redirect
from braces.views import SetHeadlineMixin
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from .models import Resource
from .forms import ResourceCreateForm, ResourceUpdateForm
from myaccount.models import SavedResource
from django.views.decorators.csrf import csrf_protect



#def ResourceAllListView(request):
#    queryset = Resource.objects.all()
#    context = {
#        "queryset": queryset,
#    }
#    return render(request, "upload/resource_list.html", context)

class ResourceAllListView(ListView):
    context_object_name = 'resources'
    template_name = 'resources/resource_list.html'
    
    def get_queryset(self):
        #resources = Resource.objects.all()
        
        return resources


class ResourceDetailView(DetailView):
    model = Resource
    context_object_name = 'resource'
    template_name = 'upload/resource_detail.html'

    def get_object(self):
        resource = super(ResourceDetailView, self).get_object()
        self.headline = str(resource.title)
        return resource

    def get_context_data(self, **kwargs):
        context = super(ResourceDetailView, self).get_context_data(**kwargs)
        return context
    
#@csrf_protect
#def ResourceCreateView(request, self):
#    if request.method == 'POST':
#        form = ResourceCreateForm(request.POST, request.FILES)        
#        if form.is_valid():
#            video = Resource(video_upload = request.FILES['video_upload'])
#            video.save()
#            form.instance.created_by = self.request.User
#            return redirect('login')
            #return HttpResponseRedirect('register')
#    else:
#        form = ResourceCreateForm()
#    return render(request, 'resource_detail.html', {'form': form})
        
       
class ResourceCreateView(CreateView):
    form_class = ResourceCreateForm
    model = Resource
    headline = 'Add video'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ResourceCreateView, self).form_valid(form)

class ResourceUpdateView(UpdateView):
    form_class = ResourceUpdateForm
    model = Resource
    headline = 'Edit Resource'
    permission_required = 'resources.change_resource'
    return_403 = True


class ResourceSaveView(RedirectView):
    permanent = False

    def get_redirect_url(self, pk):
        resource = get_object_or_404(Resource, pk=pk)
        SavedResource.objects.get_or_create(user=self.request.user, resource=resource)
        return reverse_lazy('resource_detail', kwargs={'pk':pk})
        
        #if self.request.META['HTTP_REFERER']:
        #    return self.request.META['HTTP_REFERER']
        #else:
        #    return reverse_lazy('resource_detail', kwargs={'pk':pk})
