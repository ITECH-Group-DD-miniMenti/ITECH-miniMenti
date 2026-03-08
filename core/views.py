from django.shortcuts import render
from polls.models import Session
from django.shortcuts import render, redirect

def home(request):
    return render(request, "core/home.html")

def join(request):
    if request.method == "POST":
        code = request.POST.get("code")

        try:
            session = Session.objects.get(code=code)
            return redirect("vote", code=session.code)
        except Session.DoesNotExist:
            return render(request, "core/join.html", {
                "error": "Invalid session code"
            })

    return render(request, "core/join.html")

def login_view(request):
    return render(request, "core/login.html")

def vote(request, code):
    try:
        session = Session.objects.get(code=code)
    except Session.DoesNotExist:
        return redirect("join")

    return render(request, "core/vote.html", {
        "session": session
    })

def dashboard(request):
    return render(request, "core/dashboard.html")