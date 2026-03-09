from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("join/", views.join, name="join"),
    path("vote/<str:code>/", views.vote, name="vote"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_poll/", views.create_poll, name="create_poll"),
    path("login/", views.login_view, name="login"),
    path("toggle_poll/<str:code>/", views.toggle_poll, name="toggle_poll"),
    path("export/<str:code>/", views.export_results, name="export_results"),
]