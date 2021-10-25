from django.test import TestCase
from design.models import Profile, Project
from django.contrib.auth.models import User
# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Jack")
        self.profile = Profile(user=self.user, pic="test.jpg", bio = "A description" )    

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
    def test_save(self):
        self.profile.save_profile()
        the_profile = Profile.objects.all()
        self.assertTrue(len(the_profile)>0)
    def test_delete(self):
        self.profile.save_profile()      
        self.profile.delete_profile()
        self.assertTrue(len(Profile.objects.all())==0)

class ProjectTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Jack")
        self.user.save()
        self.profile = Profile(user=self.user, pic="test.jpg", bio = "A description" )
        self.profile.save_profile()
        self.test = Project(pic="test.jpg", description="caption", owner=self.profile,)  
        self.test.save_image()  

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()
    def test_delete(self):     
        self.test.delete_image()
        self.assertTrue(len(Project.objects.all())==0)         