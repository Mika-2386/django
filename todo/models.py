from django.contrib.auth.models import AbstractUser
from django.db import models

class TaskUser(AbstractUser):
    ...



class Task (models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)