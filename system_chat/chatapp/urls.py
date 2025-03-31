from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("rooms/", views.rooms, name="rooms"),
    path("register/", views.register, name="signup"),
    path("<str:slug>/", views.room, name="room"),
]
