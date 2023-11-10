from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    data = {
        "1": "Arsenal",
        "2": "Aston Villa",
        "3": "Bournemouth",
        "4": "Brentford",
        "5": "Brighton & Hove Albion",
        "6": "Burnley",
        "7": "Chelsea",
        "8": "Crystal Palace",
        "9": "Everton",
        "10": "Fulham",
        "11": "Liverpool",
        "12": "Luton Town",
        "13": "Manchester City",
        "14": "Manchester United",
        "15": "Newcastle United",
        "16": "Nottingham Forest",
        "17": "Sheffield United",
        "18": "Tottenham Hotspur",
        "19": "West Ham United",
        "20": "Wolverhampton Wanderers"
    }
    context = {"page": "homepage", "detail": "show all team", "data": data}
    return render(request, "audience/homepage.html", context)

def team_detail(request, team_id):
    data = {
        "team": team_id,
        "team_name": "Arsenal",
        "rank": 1,
        "win": 10,
        "draw": 10,
        "player": [
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
