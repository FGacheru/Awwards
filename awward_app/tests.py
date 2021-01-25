from django.test import TestCase
from .models import Profile,Project
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.frank = User(username = 'frank',email = 'gacheruf12@gmail.com')
        self.frank = Profile(user = Self.frank,user = 1,Bio = 'tests',photo = 'test.jpg',date_craeted='dec,01.2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.frank,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.frank.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)
        
        
class ProjectTestCase(TestCase):
    def setUp(self):
        self.new_post = Projects(title = 'testT',projectscreenshot = 'test.jpg',description = 'testD',user = frank,projecturl = 'https://test.com',datecreated='Jan,25.2021')


    def test_save_project(self):
        self.new_post.save_project()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        pictures = Projects.objects.all()
        self.assertEqual(len(pictures),1