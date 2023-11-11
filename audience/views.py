from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    data = {
        "Arsenal": {
            "rank": 1
        },
        "Aston Villa": {
            "rank": 2
        }
    }
    context = {"page": "homepage", "detail": "show all team", "data": data}
    return render(request, "audience/homepage.html", context)

def team_detail(request, team_id):
    data = {
        "team": team_id,
        "team_name": "Arsenal",
        "rank": 1,
        "win": 10,
        "Draw": 10,
        "Player": [
            {
                "player_code": "A",
                "number": 10,
                "goal": 10,
                "match": 10
            },
            {
                "player_code": "US",
                "number": 1,
                "goal": 10,
                "match": 10
            }
        ]
    }
    context = {"page": "team_detail", "detail": f"show detail on each team(team_id ={team_id}).", "data": data}
    return render(request, "audience/team_detail.html", context)