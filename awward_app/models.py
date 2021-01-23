from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    Profile = models.ImageField(upload_to='profile/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    more_info = models.TextField(blank=False, null=True)
    
    def __str__(self)
        return self.bio
    
    def save_user(self)
        self.save()
     
    @receiver(post_save, sender=User)  
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)
            
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs)
    isinstance.profile.save()
    