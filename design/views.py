from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from design.models import Project, Rating
from design.forms import NewProjForm, ProfUpdateForm, RateForm
from django.db.models.base import ObjectDoesNotExist
from rest_framework.views import APIView

from .models import  Project, Profile
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, "index.html", {"projs":projects,})

@login_required(login_url='/accounts/login/')
def you(request):
    current_prof = request.user.profile
    projs = Project.objects.filter(owner = current_prof).all()
    return render(request, "you.html", {"projs":projs}) 

@login_required(login_url='/accounts/login/')
def profile(request, id):
    user = User.objects.get(id=id)
    projs= Project.objects.filter(owner = user.profile).all()
    return render(request, "profile.html", {"projs":projs, "user":user}) 

@login_required(login_url='/accounts/login/')
def new_proj(request):
    current_user = request.user.profile    
    if request.method == "POST":
      form = NewProjForm(request.POST, request.FILES)
      if form.is_valid():
        post = form.save(commit=False)
        post.owner = current_user
        post.save()
        return redirect('you')
    else:
        form = NewProjForm()
    return render(request, 'new_proj.html', {"form": form})            


def search(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        projs = Project.searcher(search_term)
        title = f"For {search_term}"

        return render(request, 'search.html', {"title":title, "projs":projs})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})  

@login_required(login_url='/accounts/login/')
def single(request, id):
    current_prof = request.user.profile
    project = Project.objects.get(id=id)
    ratings = Rating.objects.filter(project = id)
    design = []
    usability = []
    content = []

    for r in ratings:
        design.append(r.design)
        usability.append(r.usability)
        content.append(r.content)

    if len(design)>0 or len(content)>0 or len(usability)>0:    
        avg_design = sum(design)//len(design)
        avg_usability = sum(usability)//len(usability)
        avg_content = sum(content)//len(content)
    else:    
        avg_design = 0
        avg_usability = 0
        avg_content = 0



    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.owner = current_prof
            vote.project = project
            vote.save()
            return redirect('home')
    else:
        form = RateForm()            
    return render(request,"project.html", {"project":project, "design": avg_design, "content": avg_content, "usability": avg_usability, "form":form, "ratings":ratings})         
            

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_profile = request.user.profile
    if request.method == "POST":
      form = ProfUpdateForm(request.POST, request.FILES, instance=request.user.profile)
      if form.is_valid():
        image = form.cleaned_data['pic']
        bio = form.cleaned_data['bio']
        contacts = form.cleaned_data['contacts']
        current_profile.bio = bio
        current_profile.contacts = contacts
        current_profile.pic = image
        current_profile.save()
        return redirect('you')
    else:
        form = ProfUpdateForm()
    return render(request, 'prof_update.html', {"form": form})     

class ProjList(APIView):
    def get(self, request, format=None):
        all_projs = Project.objects.all()
        serializers = ProjectSerializer(all_projs, many=True)
        return Response(serializers.data) 
class ProfList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)     
