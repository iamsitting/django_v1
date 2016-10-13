from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

sendfile_storage = FileSystemStorage(location=settings.SENDFILE_ROOT)
# Create your models here.
class Download(models.Model):
    file = models.FileField(upload_to='download', storage=sendfile_storage)

    @models.permalink
    def get_absolute_url(self):
        return ('download', [self.pk], {})

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
