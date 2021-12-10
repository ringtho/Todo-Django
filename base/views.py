from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm

def getTasks(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request,'base/task_list.html', context)

def getTask(request,pk):
    task = Task.objects.get(id=pk)
    context = {"task": task}
    return render(request, 'base/task.html', context)

def createTask(request):
    form = TaskForm()
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    context = {'form': form}
    return render(request,'base/task_form.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method=="POST":
        form = TaskForm(request.POST, instance=task)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        # task.complete = request.POST.get('complete')
        if request.POST.get('complete') is None:
            task.complete = False
        else:
            task.complete = True
        task.save()
        return redirect('tasks')
    context = {"form":form}
    return render(request, 'base/task_form.html', context)
