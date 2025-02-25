from django.urls import path

from .views import c_index, index

urlpatterns = [
    path("", index, name="index"),
    path("cotton/", c_index, name="c_index"),
]
