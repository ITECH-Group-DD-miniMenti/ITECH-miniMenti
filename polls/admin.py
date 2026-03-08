from django.contrib import admin
from .models import Session, Question, Vote

admin.site.register(Session)
admin.site.register(Question)
admin.site.register(Vote)