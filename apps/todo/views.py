from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def c_index(request):
    return render(request, "c_index.html")
