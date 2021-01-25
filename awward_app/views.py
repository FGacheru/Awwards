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
    projects = Projects.get_by_author(author)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('user_profile')
        
    else:
        form = ProfileForm()    
    return render(request, 'all-awwards/profile.html', {"form":form, "projects":projects})


@login_required(login_url='/accounts/login')
def search(request):
    projects = Projects.objects.all()
    parameter = request.GET.get("project")
    result = Projects.objects.filter(project_name__icontains=parameter)
    print(result)
    return render(request, 'all-awwards/search.html', locals())


class ProjectsList(APIView):
    def get(self, request, format=None):
        all_merch = Projects.objects.all()
        serializers = ProjectsSerializer(all_merch, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = (IsAdminOrReadOnly,)
    
class ProjectsDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_projects(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return Http404
        
    def get(self, request, pk, format=None):
        project = self.get_projects(pk)
        serializers = ProjectsSerializer(project)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        project = self.get_projects(pk)
        serializers = ProjectsSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        project = self.get_projects(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = (IsAdminOrReadOnly,)
    