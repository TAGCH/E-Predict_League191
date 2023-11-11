from django.db import models
# Create your models here.


class TeamList(models.Model):
    """
    Model that contain all team data.
    """
    team = models.CharField(max_length=300)
    win = models.IntegerField()
    lose = models.IntegerField()
    draw = models.IntegerField()
    point = models.IntegerField()
    home_won = models.IntegerField()
    home_lose = models.IntegerField()
    home_draw = models.IntegerField()
    away_won = models.IntegerField()
    away_lose = models.IntegerField()
    away_draw = models.IntegerField()
    home_goal = models.IntegerField()
    away_goal = models.IntegerField()
    home_against = models.IntegerField()
    away_against = models.IntegerField()
    goal = models.IntegerField()
    goal_against = models.IntegerField()



class TeamDetail(models.Model):
    """Class of Team. Contain a specific team detail."""
    team_name = models.ForeignKey(TeamList, on_delete=models.CASCADE)
    player_name = models.ForeignKey()