from django.shortcuts import render, redirect
from .models import Task
from .forms import NewTaskForm, UpdateTaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    template_name = "tasks/index.html"
    context = {
        "tasks": tasks
    }
    return render(request, template_name, context)

def detail(request, pk):
    task = Task.objects.get(pk=pk)
    template_name = "tasks/detail.html"
    context = {
        "task": task
    }
    return render(request, template_name, context)

def new(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = NewTaskForm()

    template_name = "tasks/new.html"
    context = {
        'form':form
    }
    return render(request, template_name, context)

def update(request, pk):
    task = Task.objects.get(pk=pk)
    form = UpdateTaskForm(request.POST, instance=task)
    template_name = "tasks/update.html"
    context = {
        "task": task,
        "form": form
    }
    return render(request, template_name, context)


def delete(request, pk):
    task = Task.objects.get(pk=pk)

    task.delete()
    return redirect("/")