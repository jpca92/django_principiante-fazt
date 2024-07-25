from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import *
from .forms import *

# Create your views here.
def hello (request, username):
    print(username)
    return HttpResponse('Hello world %s' %username)
    

def about (request):
    username = 'fazt'
    return render(request, 'about.html', {'username':username})

def index (request, id):
    result = id + 100 *2
    response_text = f'Index Page {id}, result: {result}'
    return HttpResponse(response_text)

def project(request):
    projects = list(Project.objects.values())
    # Para pasar la query
    # Esto arrojaria en el html un queryset
    # projects = Project.objects.all()

    # return JsonResponse(projects, safe = False)
    return render(request, 'projects.html', {'projects': projects})

def task (request):
    # task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id = id)
    # return HttpResponse('tasks: %s' %task.title)
    
    #para renderizar en el ciclo for todas las tareas
    # opcion 1
    # tasks = list(Task.objects.values())
    # opcion 2
    tasks = Task.objects.all()
    return render (request , 'tasks.html', {'tasks': tasks})

def home (request):
    return render(request , 'home.html')

# def create_task (request):
#     Task.objects.create(title = request.GET['title'], description= request.GET['description'],
#                         project=1)
#     return render (request, 'create_task.html', {'form': CreateNewTask()})

def create_task (request):
    return render (request, 'create_task.html', {'form':CreateNewTask})