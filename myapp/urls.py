from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta raíz
    path('hello/<str:username>/', views.hello, name='hello'),  # Añadido '/' al final
    path('about/', views.about, name='about'),
    path('index/<int:id>/', views.index, name='index'),  # Añadido '/' al final
    path('projects/', views.project, name='projects'),
    path('tasks/', views.task, name='tasks'),
    path('create_task/', views.create_task),
    path('create_project/', views.create_project),
]
