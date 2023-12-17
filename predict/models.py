from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)


class Prediction(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score_team1 = models.IntegerField()
    score_team2 = models.IntegerField()
