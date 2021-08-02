from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "users/index.html")

def about(request):
    return render(request, "users/about.html")

def forms(request):
    return render(request, "users/forms.html")