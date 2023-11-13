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
        "6": "Chelsea",
        "7": "Crystal Palace",
        "8": "Everton",
        "9": "Fulham",
        "10": "Leeds United",
        "11": "Leicester City",
        "12": "Liverpool",
        "13": "Manchester City",
        "14": "Manchester United",
        "15": "Newcastle United",
        "16": "Nottingham Forest",
        "17": "Southampton",
        "18": "Tottenham Hotspur",
        "19": "West Ham United",
        "20": "Wolverhampton Wanderers"
    }
    context = {"page": "homepage", "detail": "show all team", "data": data}
    return render(request, "audience/homepage.html", context)

def team_detail(request, team_id):
    player_filename = "audience/static/audience/data/player_with_team_id.csv"
    team_filename = "audience/static/audience/data/team_detail.csv"

    players = []
    team_details = {}

    # Load player data
    with open(player_filename, 'r', encoding='utf-8') as player_file:
        player_rows = csv.DictReader(player_file)
        for player_row in player_rows:
            team_id_str = player_row.get('team_id', '')
            if team_id_str and int(team_id_str) == team_id:
                players.append(player_row)

    # Load team detail data
    with open(team_filename, 'r', encoding='utf-8') as team_file:
        team_rows = csv.DictReader(team_file)
        for team_row in team_rows:
            team_details[team_row['team_id']] = team_row

    # Get team details for the specified team_id
    team_detail = team_details.get(str(team_id), {})

    context = {
        "page": "team_detail",
        "detail": "show all players and team details for the team",
        "team_id": team_id,
        "players": players,
        "team_detail": team_detail,
    }

    return render(request, "audience/team_detail.html", context)

def player_information(request, player_id):
    data = {}
    filename = "audience/static/audience/data/player_with_team_id.csv"
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for r in rows:
            if int(r['Id']) == player_id:
                data = r

    context = {"page": "player_information", "detail": "show all player infos", "data": data}
    return render(request, "audience/player_information.html", context)

