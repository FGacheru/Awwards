from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    date = dt.date.today()
    projects = Projects.objects.all()
    return render(request, 'all-awwards/home.html', {"date":date, "projects":projects})

@login_required(login_url='/accounts/login')
def project(request, id):

    try:
        project = Projects.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()    
    
    return render(request, "all-awwards/project.html", {"project":project})

@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('home')

    else:
        form = UploadForm()
    return render(request, 'all-awwards/upload_project.html', {"form":form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    author = current_user
    projects = Projects.author
    
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.save()
            
        return redirect ('profile')
    else:
        form = ProfileForm()
    return render(request, 'all-awwards/profile.html', {"form":form, "projects":projects})


@login_required(login_url='/accounts/login')
def search(request):
    projects = Projects.objects.all()
    parameter = request.GET.get("project")
    result = Projects.objects.filter(project_name__icontains=parameter)
    print(result)
    return render(request, 'search.html', locals())
        
