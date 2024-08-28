from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Project
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

# Custom Signup Form with Email

def home(request):
    return render(request, 'portfolio/home.html')

#@login_required
def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def contacts(request):
    return render(request, 'portfolio/contacts.html')

