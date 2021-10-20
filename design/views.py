from django.shortcuts import render

# Create your views here.
def home(request):
    val = "Welcome"
    return render(request, "index.html", {"val":val,})