from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

#@login_required
def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'portfolio/login.html')

def user_logout(request):
    logout(request)
    #return render(request, 'portfolio/login.html')
    return redirect('home')
