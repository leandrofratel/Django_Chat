from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room, name='chat_room'),  # Rota para a sala de chat
]