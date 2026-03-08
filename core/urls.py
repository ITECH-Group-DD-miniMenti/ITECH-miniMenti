from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("join/", views.join, name="join"),
    path("login/", views.login_view, name="login"),
    path("vote/", views.vote, name="vote"),
    path("dashboard/", views.dashboard, name="dashboard"),
]