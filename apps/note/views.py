from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from .forms import NoteForm
from .models import Note


def index(request) -> HttpResponse:
    return render(request, "index.html")


def c_index(request):
    form = NoteForm()
    return render(request, "c_index.html", {"notes": Note.objects.all(), "form": form})


def create_note(request) -> HttpResponse:
    form = NoteForm(request.POST)
    if form.is_valid():
        note = form.save(commit=False)
        note.author = request.user
        note.save()
        return redirect("home")
    return render(request, "components/note/list.html", {"data": Note.objects.all()})


def delete_note(request, id) -> HttpResponse:
    note = get_object_or_404(Note, id=id)
    note.delete()
    return render(request, "components/note/list.html", {"data": Note.objects.all()})
