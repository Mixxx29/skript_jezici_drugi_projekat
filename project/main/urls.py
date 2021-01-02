from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/<username>/', views.user, name='user'),
    path('projects/<id>/', views.project, name='project'),
    path('projects/like/<id>/', views.like, name='like'),
    path('projects/dislike/<id>/', views.dislike, name='dislike'),
    path('add/', views.add, name='add'),
]