from django import forms
from .models *

class ProfileForm(forms.ModelForm)
    class Meta:
        model = Profile
        fields = ('profile', 'bio', 'user_id', 'more_info')
        
class UploadForm(forms.ModelForm):
    class Meta:
        model= Projects
        fields = ('project_name', 'image', 'description', 'pub_date', 'author', 'author_photo', 'url')