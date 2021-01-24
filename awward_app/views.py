from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly


# Create your views here.
def home(request):
    date = dt.date.today()
    heading = "Welcome to Awward Application"
    Projects = Projects.objects.all()
    return render(request, 'home.html', {"date":date, "heading":heading, "projects":projects})
