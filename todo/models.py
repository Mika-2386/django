from django.db import models

# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length=180, description=180)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)