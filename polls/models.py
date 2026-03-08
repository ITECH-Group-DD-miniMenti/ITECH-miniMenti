from django.db import models
from django.contrib.auth.models import User


class Session(models.Model):
    title = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200, blank=True)
    option_d = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.text


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=1)  # A / B / C / D

    def __str__(self):
        return f"{self.question} - {self.choice}"