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
        note = form.save(commit=False)
        note.author = request.user
        note.save()
    return render(request, "components/note/list.html", {"data": Note.objects.all()})


def delete_task(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return render(request, "components/note/list.html", {"data": Note.objects.all()})
