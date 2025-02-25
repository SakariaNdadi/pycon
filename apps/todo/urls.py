from django.urls import path

from .views import c_index, create_task, index

urlpatterns = [
    path("", index, name="index"),
    path("cotton/", c_index, name="c_index"),
    path("create/", create_task, name="create_task"),
]
