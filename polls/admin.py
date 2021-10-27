# /home/syl1/private/Pgm/djo1/top/polls/admin.py
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
