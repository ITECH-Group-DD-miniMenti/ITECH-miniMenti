from django.shortcuts import render
from polls.models import Session, Question, Vote
from django.shortcuts import render, redirect
from django.db.models import Count

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
        question = Question.objects.filter(session=session).first()
    except Session.DoesNotExist:
        return redirect("join")

    if not question:
        return render(request, "core/vote.html", {
            "session": session,
            "question": None
        })

    if request.method == "POST":
        choice = request.POST.get("choice")

        if choice in ["A", "B", "C", "D"]:
            Vote.objects.create(
                question=question,
                choice=choice
            )
            return render(request, "core/vote.html", {
                "session": session,
                "question": question,
                "success": "Your vote has been submitted."
            })

    return render(request, "core/vote.html", {
        "session": session,
        "question": question
    })


def dashboard(request):
    question = Question.objects.first()

    if not question:
        return render(request, "core/dashboard.html", {
            "question": None
        })

    votes = Vote.objects.filter(question=question)

    results = {
        "A": votes.filter(choice="A").count(),
        "B": votes.filter(choice="B").count(),
        "C": votes.filter(choice="C").count(),
        "D": votes.filter(choice="D").count(),
    }

    return render(request, "core/dashboard.html", {
        "question": question,
        "results": results
    })