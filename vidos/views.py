from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import FormView
from django.shortcuts import HttpResponseRedirect, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic import ListView




from videos.models import video, Category
from myaccount.models import MyUser
from myaccount.forms import RegisterForm, LoginForm
#from .forms import LoginForm


        
#@login_required
def home(request):
       
    
    videos = video.objects.all()
    embeds = []
    
    for vid in videos:
        code = mark_safe(vid.embed_code)
        embeds.append("%s" %(code))
               
    context={
        
        "videos": videos,
        "the_embeds": embeds,
        "a_code": mark_safe(video.objects.all()[0].embed_code)        
    }
    return render(request, "home.html",context)
    #else:
        #return HttpResponseRedirect('/login')





    
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def auth_login(request):
    form = LoginForm(request.POST or None)
    #next_url = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #username = request.POST['username']
        #password = request.POST['password']
        #print (username, password)
        
        user = authenticate(username=username, password=password)
        print (authenticate(username=username, password=password))
        if user is not None:
            login(request, user)
            return redirect("register")
            #if next_url is not None:
              #return HttpResponseRedirect(next_url)
            #return HttpResponseRedirect("/")
    #action_url = reverse("login")
    #title = "login"
        
        
    context={
        "form": form,
    }    
    return render(request, "login.html",context)


def user_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password2']
        new_user = MyUser()
        new_user.username = username
        new_user.email = email
        new_user.set_password(password)
        new_user.save()
        return redirect('login')
        print(username, email, password)
    action_url = reverse("register")
    title = "Register"
    
        
    context={
        "form": form,
        "action_value": action_url,
        "submit_btn_value": "Register",           
    }
    return render(request, "register.html",context)

def google_Seo(request):
    return render(request, "google490de29a933d2b95.html")
    
    
    



                  



