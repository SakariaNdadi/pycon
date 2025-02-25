from django.shortcuts import render

from .forms import TaskForm
from .models import Task


def index(request):
    return render(request, "index.html")


def c_index(request):
    form = TaskForm()
    return render(request, "c_index.html", {"tasks": Task.objects.all(), "form": form})


def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        task.save()
    return render(request, "components/task/list.html", {"data": Task.objects.all()})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return render(request, "components/task/list.html", {"data": Task.objects.all()})
