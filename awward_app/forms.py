from django import forms
from .models *

class ProfileForm(forms.ModelForm)
    class Meta:
        model = Profile
        fields = ('')
        
class UploadForm(forms.ModelForm):
    class Meta:
        model= Projects
        fields = ('')