from rest_framework import serializers
from .models import *

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'project_name', 'image', 'description', 'pub_date', 'author', 'author_photo', 'url')
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =('id','profile', 'bio', 'user_id', 'more_info')