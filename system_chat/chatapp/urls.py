from . import views
from django.urls import path
from .views import create_room
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("rooms/", views.rooms, name="rooms"),
    path("register/", views.register, name="signup"),
    path("<str:slug>/", views.room, name="room"),
    path("create_room/", create_room, name="create_room")
]
