from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Audio_note(models.Model):
    title = models.CharField(max_length=50)
    note = models.TextField(blank=True,null=True)
    audio_file = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

