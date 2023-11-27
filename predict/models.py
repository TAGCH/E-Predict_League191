from django.db import models


# Create your models here.


class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    score_team1 = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    score_team2 = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    date = models.DateField()
