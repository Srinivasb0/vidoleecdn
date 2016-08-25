from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Document
from .forms import DocumentForm


@login_required
def list(request):
    # Handle file upload
    if request.method == 'POST':
        #form = DocumentForm(request.POST, request.FILES)
        form = DocumentForm(request.POST)
        if form.is_valid():
    
            #newdoc = Document(docfile = request.FILES['docfile', 'title',])
            #newdoc.save()            
            #messages.success(request, "Successfully Created")
            newdoc = form.save()
            #return redirect(Document)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myaccount.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request, 
        'lists.html',
        {'documents': documents, 'form': form})
    

def index(request):
    return render(request, 'index.html')

def Document_delete(request):
    instance = get_object_or_404(Document)
    instance.delete()
    return render(request, 'lists.html')
    
