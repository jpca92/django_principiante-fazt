from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

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
    return render(request, 'projects/projects.html', {'projects': projects})

def task (request):
    # task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id = id)
    # return HttpResponse('tasks: %s' %task.title)
    
    #para renderizar en el ciclo for todas las tareas
    # opcion 1
    # tasks = list(Task.objects.values())
    # opcion 2
    tasks = Task.objects.all()
    return render (request , 'tasks/tasks.html', {'tasks': tasks})

def home (request):
    return render(request , 'home.html')

# def create_task (request):
#     Task.objects.create(title = request.GET['title'], description= request.GET['description'],
#                         project=1)
#     return render (request, 'create_task.html', {'form': CreateNewTask()})

def create_task (request):
    if request.method == 'GET':
        return render (request, 'tasks/create_task.html', {'form':CreateNewTask()})
    else:
        # print(request.GET['title'])
        # print(request.GET['description'])
        Task.objects.create(title=request.POST['title'], description = request.POST['description'], project_id=1)
        return redirect('tasks')

# def create_project(request):
#     if request.method == 'GET':
#         return render (request, 'projects/create_project.html', {'form': CreateNewProject()})
#     else:
#         print(request.POST)
#         return render (request, 'projects/create_project.html', {'form': CreateNewProject()})

def create_project(request):
    if request.method == 'GET':
        return render (request, 'projects/create_project.html', {'form': CreateNewProject()})
    else:
        # print(request.POST)
        Project.objects.create(name= request.POST['name'])
        redirect ('projects')
