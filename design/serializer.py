from rest_framework import serializers
from .models import Profile, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','pic', 'description', 'link', 'owner') 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','bio','pic', 'contacts',) 