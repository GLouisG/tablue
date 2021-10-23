from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

           
class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)    
      bio = models.TextField(max_length=500, default=f'This is my bio, Welcome!')
      contacts = models.TextField(max_length=500, default=f'Contacts:')
            

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
      picture = models.ImageField(upload_to='photos/', default='SOMETHING')
      description = models.TextField()
      link = models.TextField()
      owner = models.ForeignKey('Profile', on_delete=models.CASCADE)       

      def save_project(self):
            '''Saves project'''
            self.save()
      def delete_project(self):
            '''Deletes project''' 
            self.delete() 
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