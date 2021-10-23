from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

           
class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)    
      bio = models.TextField(max_length=500, default=f'This is my bio, Welcome!')
      contacts = models.TextField(max_length=500, default=f'Contacts:')
      pic = models.ImageField(upload_to = 'profiles/', default='profile.jpg')      

      def __str__(self):
            return f'Profile {self.user.username}'
      def save_profile(self):
            '''Saves profiles'''
            self.save()
      def delete_profile(self):
            '''Deletes profiles''' 

            self.delete()             


class Project(models.Model):
      title  = models.CharField(max_length=30)
      pic = CloudinaryField('image')
      description = models.TextField()
      link = models.TextField()
      owner = models.ForeignKey('Profile', on_delete=models.CASCADE)       

      def save_project(self):
            '''Saves project'''
            self.save()
      def delete_project(self):
            '''Deletes project''' 
            self.delete() 
      @classmethod
      def searcher(cls, search_term):
            search_term= str(search_term)
            projs = cls.objects.filter(caption__contains = search_term)
            return projs          

      def __str__(self):
            return f'Project {self.title}'               

class Rating(models.Model):
      design = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
      usability = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])                  
      content=models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)]) 
      owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
      project = models.ForeignKey('Project', on_delete=models.CASCADE)
      def __str__(self):
            return f'For project {self.project.title}'              