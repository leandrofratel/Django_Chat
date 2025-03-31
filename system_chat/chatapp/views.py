from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Room, Message

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("rooms")  # Redireciona para as salas após registro
    else:
        form = UserCreationForm()
    
    return render(request, "registration/register.html", {"form": form})

def rooms(request):
    if not request.user.is_authenticated:
        return redirect("login")  # Redireciona para login se não estiver autenticado
    
    rooms = Room.objects.all()
    return render(request, "rooms.html", {"rooms": rooms})

def room(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")

    room_name = Room.objects.get(slug=slug).name
    messages = Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html", {"room_name": room_name, "slug": slug, "messages": messages})

def custom_login(request):
    if request.user.is_authenticated:
        return redirect("rooms")  # Se o usuário já estiver logado, vá para a lista de salas

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("rooms")  # Após login bem-sucedido, vá para as salas de chat
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})