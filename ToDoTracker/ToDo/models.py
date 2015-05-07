import datetime

from django.db import models
from django.utils import timezone

class Todo(models.Model):
    todo_text = models.CharField(max_length=300)
    deadline  = models.DateField('Deadline')
    progress  = models.CharField(max_length=10)
    def __str__(self):
        return self.todo_text