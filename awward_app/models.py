from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    profile = models.ImageField(upload_to='profile/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    more_info = models.TextField(blank=False, null=True)
    
    def __str__(self):
        return self.bio
    
    def save_user(self):
        self.save()
        
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
     
    
    
class Projects(models.Model):
    project_name = models.CharField(max_length=300)
    image = CloudinaryField('images')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    author_photo = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, default='1')
    url = models.URLField()
    
    def save_project(self):
         self.save()
         
    def delete_project(self):
        self.delete()
    
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(project_name__icontains=search_term)
        return projects
    
    
    @classmethod
    def get_by_author(cls, author):
        projects = cls.objects.filter(author=author)
        return projects

    @classmethod
    def get_project(request, id):
        try:
            project = Projects.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.project_name
    
    
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description
