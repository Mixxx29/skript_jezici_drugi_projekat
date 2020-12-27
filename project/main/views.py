from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user.username)
    else:
        return redirect('main:login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('main:home')
    else:
        form = RegisterForm()

    return render(request, 'authentication/register.html', {'form' : form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=raw_password)
            if user is not None:
                auth.login(request, user)
                return redirect('main:home')
                
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form' : form})