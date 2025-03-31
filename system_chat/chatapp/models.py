from django.db import models
from django.contrib.auth.models import User

# Modelo de sala de chat
class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100, unique=True)  # Adicionando unique para garantir que o slug seja único

    def __str__(self):
        return f"Room: {self.name} | Id: {self.slug}"
    

# Modelo de mensagem no chat
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.content} | From: {self.user.username}"
