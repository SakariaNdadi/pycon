from django.shortcuts import render

from .forms import NoteForm
from .models import Note


def index(request):
    return render(request, "index.html")


def c_index(request):
    form = NoteForm()
    return render(request, "c_index.html", {"notes": Note.objects.all(), "form": form})


def create_task(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        task.save()
    return render(request, "components/task/list.html", {"data": Note.objects.all()})


def delete_task(request, id):
    task = Note.objects.get(id=id)
    task.delete()
    return render(request, "components/task/list.html", {"data": Note.objects.all()})
