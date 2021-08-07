from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "users/index.html")

def about(request):
    return render(request, "users/about.html")

def forms(request):
    return render(request, "users/forms.html")

def signup(request):
    return render(request, "users/signup.html")

def contact(request):
    return render(request, "users/contact.html")
    
def contactTechnical(request):
    return render(request, "users/technical-contact.html")

def contactGeneral(request):
    return render(request, "users/general-contact.html")