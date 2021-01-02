from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/<username>/', views.user, name='user'),
    path('projects/<int:id>/', views.project, name='project'),
    path('projects/like/<int:id>/', views.like, name='like'),
    path('projects/dislike/<int:id>/', views.dislike, name='dislike'),
    path('projects/add/', views.add, name='add'),
    path('projects/remove/<int:id>/', views.remove, name='remove'),
    path('projects/edit/<int:id>/', views.edit, name='edit'),
]