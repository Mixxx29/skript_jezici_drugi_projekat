from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Project

class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'input', 
            'placeholder' : 'Enter username...', 
            'id' : 'username'
            },
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'input', 
            'placeholder' : 'Enter password...', 
            'id' : 'password'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'input', 
            'placeholder' : 'Repeat password...', 
            'id' : 'repeat-password'
        }
    ))


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'input', 
            'placeholder' : 'Enter username...', 
            'id' : 'username'
            }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'input', 
            'placeholder' : 'Enter password...', 
            'id' : 'password'
        }
    ))


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'image', 'description']
        