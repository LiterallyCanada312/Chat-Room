from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Message(models.Model):
    message_text = models.CharField(max_length=200)

class User(AbstractUser):
    pass

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=50)