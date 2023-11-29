from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Match
from .forms import MatchPredictionForm
from datetime import datetime

import csv


def index(request):
    return HttpResponse("Hello, world. You're at the prediction page.")


def match_list(request):
    # Load the data from csv
    match_filename = 'predict/static/predict/data/fixture.csv'
    with open(match_filename, 'r', encoding='utf-8') as match_file:
        csv_reader = csv.DictReader(match_file)
        matches = list(csv_reader)

    current = datetime.now()
    upcoming_matches = [match for match in matches
                        if datetime.strptime(match['Date'], '%d/%m/%Y %H:%M') > current
                        ][:5]

    context = {'upcoming_matches': upcoming_matches}
    return render(request, 'predict/match_list.html', context)


def predict_match(request, match_id):
    # Load data from the CSV file
    csv_path = 'predict/static/predict/data/fixture.csv'
    with open(csv_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        matches = list(csv_reader)

    # Find the match with the specified match_id
    match = None
    for m in matches:
        if int(m['MatchNumber']) == match_id:
            match = m
            break

    # Check if the match was found
    if not match:
        return render(request, 'predict/predict_match_not_found.html', {'match_id': match_id})

    # Check if the match already has results
    if match['Result'] != '':
        return render(request, 'predict/predict_match_already_end.html', {'match': match})

    # Create a dynamic form based on the match information
    form = MatchPredictionForm(initial={'match_id': match_id})
    # Set labels for team names in the form
    form.set_team_labels(match['HomeTeam'], match['AwayTeam'])

    if request.method == 'POST':
        form = MatchPredictionForm(request.POST)
        if form.is_valid():
            # Process the form data (save it to a database or handle as needed)
            return redirect('match_list')  # Redirect to the match list or another page

    return render(request, 'predict/predict_match.html', {'match': match, 'form': form})
