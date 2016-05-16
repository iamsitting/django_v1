from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getEmail(self):
        return self.email
