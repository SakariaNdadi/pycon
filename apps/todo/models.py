from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    class Categories(models.TextChoices):
        WORK = "work", "Work"
        Home = "home", "Home"
        SCHOOL = "school", "School"

    content = models.TextField()
    categories = models.CharField(max_length=7, choices=Categories.choices, default=Categories.Home)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateTimeField(auto_now=True)
