from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'user_id', 'more_info')
        
class UploadForm(forms.ModelForm):
    class Meta:
        model= Projects
        fields = ('project_name', 'image', 'description','author', 'author_photo', 'url')