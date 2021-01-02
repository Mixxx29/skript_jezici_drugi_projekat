from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import RegisterForm, LoginForm, ProjectForm
from .models import Project, Like

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        projects = Project.objects.order_by('-created')
        posts = []
        for project in projects:
            try:
                project.like_set.get(user=request.user)
                posts.append(Post(project, True))
            except:
                posts.append(Post(project, False))
            
        return render(request, 'home.html', {'user' : request.user, 'posts' : posts})
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

@login_required
def logout(request):
    auth.logout(request)
    return redirect('main:login')

@login_required
def project(request, id):
    if request.method == 'GET':
        project = Project.objects.get(id=id)
        if (project == None):
            raise Http404()

        post = None
        try:
            project.like_set.get(user=request.user)
            post = Post(project, True)
        except:
            post = Post(project, False)

    return render(request, 'project.html', {'post' : post})

@login_required
def like(request, id):
    project = Project.objects.get(id=id)
    try:
        project.like_set.get(user=request.user)
    except:
        newLike = Like(user=request.user, project=project)
        newLike.save()

    return redirect('main:project', id=id)

@login_required
def dislike(request, id):
    project = Project.objects.get(id=id)
    try:
        like = project.like_set.get(user=request.user)
        like.delete()
    except:
        pass

    return redirect('main:project', id=id)

def user(request, username):
    try:
        user = User.objects.get(username=username)
        projects = user.project_set.order_by('-created')
        posts = []
        for project in projects:
            try:
                project.like_set.get(user=request.user)
                posts.append(Post(project, True))
            except:
                posts.append(Post(project, False))

        return render(request, 'user.html', {'user' : user, 'posts' : posts, 'count' : len(posts)})
    except:
        raise Http404()

@login_required
def add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            description = form.cleaned_data.get('description')
            newProject = Project(user=user, title=title, image=image, description=description)
            newProject.save()
            return redirect('main:home')

    else:
        form = ProjectForm()

    return render(request, 'add.html', {'form' : form})
        



class Post:
    def __init__(self, project, liked):
        self.project = project
        self.liked = liked