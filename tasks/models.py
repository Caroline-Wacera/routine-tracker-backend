from django.db import models
from django.contrib.auth.models import User  # built-in user model

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link task to a user
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()         # date of the task
    time = models.TimeField()         # time of the task
    completed = models.BooleanField(default=False)  # checker

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {'Done' if self.completed else 'Pending'}"
# Create your models here.
