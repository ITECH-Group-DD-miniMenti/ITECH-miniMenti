import base64
from io import BytesIO

import qrcode
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from polls.models import Session, Question, Vote

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
    if request.method == "POST":
        return redirect("dashboard")

    return render(request, "core/login.html")

def vote(request, code):
    try:
        session = Session.objects.get(code=code)
        question = Question.objects.filter(session=session).first()
    except Session.DoesNotExist:
        return redirect("join")

    if not session.is_active:
        return render(request, "core/poll_closed.html")

    if not question:
        return render(request, "core/vote.html", {
            "session": session,
            "question": None
        })

    vote_key = f"voted_{question.id}"

    if request.method == "POST":
        if request.session.get(vote_key):
            return render(request, "core/vote.html", {
                "session": session,
                "question": question,
                "error": "You have already voted.",
                "already_voted": True
            })

        choice = request.POST.get("choice")

        if choice in ["A", "B", "C", "D"]:
            Vote.objects.create(
                question=question,
                choice=choice
            )
            request.session[vote_key] = True
            return render(request, "core/vote.html", {
                "session": session,
                "question": question,
                "success": "Your vote has been submitted.",
                "already_voted": True
            })

    return render(request, "core/vote.html", {
        "session": session,
        "question": question,
        "already_voted": request.session.get(vote_key, False)
    })


def dashboard(request):
    sessions = Session.objects.order_by("-created_at")

    poll_data = []

    for session in sessions:
        question = Question.objects.filter(session=session).first()

        if question:
            votes = Vote.objects.filter(question=question)

            results = {
                "A": votes.filter(choice="A").count(),
                "B": votes.filter(choice="B").count(),
                "C": votes.filter(choice="C").count(),
                "D": votes.filter(choice="D").count(),
            }

            total_votes = sum(results.values())

            percentages = {
                "A": (results["A"] / total_votes * 100) if total_votes else 0,
                "B": (results["B"] / total_votes * 100) if total_votes else 0,
                "C": (results["C"] / total_votes * 100) if total_votes else 0,
                "D": (results["D"] / total_votes * 100) if total_votes else 0,
            }

            join_url = request.build_absolute_uri(f"/vote/{session.code}/")

            qr = qrcode.make(join_url)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode()

            poll_data.append({
                "session": session,
                "question": question,
                "results": results,
                "percentages": percentages,
                "total_votes": total_votes,
                "qr": qr_base64,
                "join_url": join_url,
            })

    return render(request, "core/dashboard.html", {
        "poll_data": poll_data
    })

def create_poll(request):
    if request.method == "POST":
        title = request.POST.get("title")
        question_text = request.POST.get("question_text")
        option_a = request.POST.get("option_a")
        option_b = request.POST.get("option_b")
        option_c = request.POST.get("option_c")
        option_d = request.POST.get("option_d")

        host = User.objects.first()

        session = Session.objects.create(
            title=title,
            host=host,
            is_active=True
        )

        Question.objects.create(
            session=session,
            text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d
        )

        return redirect("dashboard")

    return render(request, "core/create_poll.html")

def toggle_poll(request, code):
    session = Session.objects.get(code=code)

    session.is_active = not session.is_active
    session.save()

    return redirect("dashboard")