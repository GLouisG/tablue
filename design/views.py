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
    return render(request, "profile.html", {"projs":projs, "user":user}) 

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

def single(request, id):
    current_prof = request.user.profile
    try:
        project = Project.objects.get(id=id)
        ratings = Rating.objects.filter(project = id)
        if Rating.objects.filter(owner = current_prof, project = id).first() is None:
            if request.method == "POST":
                form = RateForm(request.POST)
                if form.is_valid():
                    vote = form.save(commit=False)
                    vote.owner = current_prof
                    vote.project = id
                    vote.save()
                    return redirect('profile')
                else:
                    form = RateForm()            

            

    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})    

def update_profile(request):
    current_profile = request.user.profile
    if request.method == "POST":
      form = NewProjForm(request.POST, request.FILES, instance=request.user.profile)
      if form.is_valid():
        image = form.cleaned_data['pic']
        bio = form.cleaned_data['bio']
        contacts = form.cleaned_data['contacts']
        current_profile.bio = bio
        current_profile.contacts = contacts
        current_profile.pic = image
        current_profile.save()
        return redirect('profile')
    else:
        form = NewProjForm()
    return render(request, 'prof_update.html', {"form": form})     