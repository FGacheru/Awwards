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
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    date = dt.date.today()
    heading = "Welcome to Awward Application"
    projects = Projects.objects.all()
    return render(request, 'all-awwards/home.html', {"date":date, "heading":heading, "projects":projects})

@login_required(login_url='/accounts/login')
def project(request, id):

    try:
        project = Projects.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()    
    
    return render(request, "all-awwards/project.html", {"project":project})

@login_required(login_url='/accounts/login/')
def upload_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'all-awwards/upload_project.html', {"form":form})
