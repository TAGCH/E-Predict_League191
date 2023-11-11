from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import csv

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

def team_detail(request, team):
    data = {}
    filename = "audience/static/audience/data/team_summary.csv"
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for r in rows:
            if r['Team'] == team:
                data = r

    filename = "audience/static/audience/data/players.csv"
    with open(filename, 'r', encoding='utf-8') as player_file:
        rows = csv.DictReader(player_file)
        player_count = 0
        for r in rows:
            if r['Team'].replace(" ", "") == team:
                data[f"player_number{player_count}"] = r["Name"]
                player_count += 1

    context = {
                "page": "team_detail",
                "detail": f"show detail on each team(team_name ={team}).",
                "data": data,
                "team": data["Team"]
                }
    return render(request, "audience/team_detail.html", context)

def player_information(request, player_id):
    data = {}
    filename = "audience/static/audience/data/players.csv"
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for r in rows:
            if int(r['Id']) == player_id:
                data = r

    context = {
                "page": "player_information",
                "detail": "show all player infos",
                "data": data
                }
    return render(request, "audience/player_information.html", context)


