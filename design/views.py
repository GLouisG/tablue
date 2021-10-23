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

def profile(request, id):
    user = User.objects.get(id=id)
    projs= Project.objects.filter(owner = user.profile).all()
    return render(request, "you.html", {"projs":projs, "user":user}) 

def new_proj(request):
    current_user = request.user.profile    
    if request.method == "POST":
      form = NewProjForm(request.POST, request.FILES)
      if form.is_valid():
        post = form.save(commit=False)
        post.owner = current_user
        post.save()
        return redirect('profile')
    else:
        form = NewProjForm()
    return render(request, 'new_proj.html', {"form": form})            

def search(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched = Project.searcher(search_term)
        title = f"For {search_term}"

        return render(request, 'search.html', {"title":title, "projs":searched})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    