from django.contrib import admin

from design.models import Profile, Project, Rating

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rating)