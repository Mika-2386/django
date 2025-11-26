from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title