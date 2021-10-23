from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

           
class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)    
      bio = models.TextField(max_length=500, default=f'This is my bio, Welcome!')
      contacts = models.TextField(max_length=500, default=f'Contacts:')
      