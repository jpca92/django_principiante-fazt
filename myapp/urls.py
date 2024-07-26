from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('hello/<str:username>/', views.hello, name='hello'), 
    path('about/', views.about, name='about'),
    path('projects/', views.project, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    path('tasks/', views.task, name='tasks'),
    path('create_task/', views.create_task, name= 'create_task'),
    path('create_project/', views.create_project, name = 'create_project'),
]
