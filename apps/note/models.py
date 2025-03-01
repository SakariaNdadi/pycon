from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Note(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    created_at = models.DateTimeField(auto_now=True)
