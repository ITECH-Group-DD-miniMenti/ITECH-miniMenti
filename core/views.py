from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def join(request):
    return render(request, "core/join.html")

def login_view(request):
    return render(request, "core/login.html")

def vote(request):
    return render(request, "core/vote.html")

def dashboard(request):
    return render(request, "core/dashboard.html")