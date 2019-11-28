from django.contrib.auth import get_user_model
from django.db import models
from gamecrush.models import User

class Message(models.Model):
    id_auth = models.IntegerField()
    room = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_auth

    def last_10_messages(id_room):
        return Message.objects.filter(room = id_room).order_by('-timestamp').all()[:10]
