from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Project
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

# Custom Signup Form with Email
'''
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_group, created = Group.objects.get_or_create(name='Users')
            user.groups.add(user_group)
        return user
'''    

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after signup.
    else:
        form = UserCreationForm()
    return render(request, 'portfolio/signup.html', {'form': form})

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
