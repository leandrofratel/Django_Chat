from django.db import models
from django.contrib.auth.models import User

# Modelo de sala de chat
class Room(models.Model):
    """
    Sala de Chat:
    - name: Nome da Sala
    - slug: Nome de identificação na url
    """
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f"Room: {self.name} | Id: {self.slug}"
    

# Modelo de mensagem no chat
class Message(models.Model):
    """
    Cria as mensagens para a sala:
    - user: Usuário
    - content: Conteúdo da mensagem
    - room: Sala onde será armazenada
    - created_on: Data da criação
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content}"
