from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
