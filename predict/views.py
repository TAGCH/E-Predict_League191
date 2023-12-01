from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Match, Prediction
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


@login_required
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

    form = MatchPredictionForm(initial={'match_id': match_id})
    form.set_team_labels(match['HomeTeam'], match['AwayTeam'])

    if request.method == 'POST':
        form = MatchPredictionForm(request.POST)
        if form.is_valid():
            # Get or create a Prediction object for the user and match
            prediction, created = Prediction.objects.get_or_create(
                user=request.user,
                match_id=int(match_id),
                defaults={
                    'score_team1': form.cleaned_data['score_team1'],
                    'score_team2': form.cleaned_data['score_team2'],
                }
            )

            # If the prediction already exists, update the scores
            if not created:
                prediction.score_team1 = form.cleaned_data['score_team1']
                prediction.score_team2 = form.cleaned_data['score_team2']
                prediction.save()

            messages.success(request, 'Prediction successful!')

            return redirect('predict:match_list')  # Redirect to the match list or another page

    predict_user = Prediction.objects.filter(match_id=match_id)

    return render(request, 'predict/predict_match.html', {'match': match, 'form': form, 'predict_user': predict_user})
