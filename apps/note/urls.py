from django.urls import path

from .views import c_index, create_note, delete_note, index

urlpatterns = [
    path("", index, name="index"),
    path("cotton/", c_index, name="home"),
    path("create/", create_note, name="create_note"),
    path("delete/<int:id>", delete_note, name="delete_note"),
]
