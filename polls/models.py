from django.db import models
# home/syl1/private/Pgm/djo1/top/polls/models.py
# for  "gettings started with django detailed  comments" see 
# home/syl1/private/Pgm/djo1/top/polls/models_tut3.py

import datetime
from django.utils import timezone
# Create your models here.
from django.db import models


class Question(models.Model):
    # __str__ methods almost mandatory because divers inclusiv of admin
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now= timezone.now()
        return  now - datetime.timedelta(days=1) <= self.pub_date <= now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    # __str__ methods almost mandatory because divers inclusiv of admin
    def __str__(self):
        return self.choice_text
    # to get use to the time business
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
