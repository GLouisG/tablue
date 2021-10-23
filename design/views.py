from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import redirect, render

from design.models import Project, Rating
from design.forms import NewProjForm, RateForm
from django.db.models.base import ObjectDoesNotExist
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, "index.html", {"projs":projects,})

def you(request):
    current_prof = request.user.profile
    projs = Project.objects.filter(owner = current_prof).all()
    return render(request, "you.html", {"projs":projs,}) 