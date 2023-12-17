from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Match, Prediction
from .forms import MatchPredictionForm
from datetime import datetime

import csv


def match_list(request):
    current_time = datetime.now()
    upcoming_matches = Match.objects.filter(date__gt=current_time)[:5]

    context = {'upcoming_matches': upcoming_matches}
    return render(request, 'predict/match_list.html', context)


@login_required
def predict_match(request, match_id):
    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        return render(request, 'predict/predict_match_not_found.html', {'match_id': match_id})

    prediction, created = Prediction.objects.get_or_create(
        user=request.user,
        match=match,
        defaults={
            'score_team1': 0,  # Set default values or adjust as needed
            'score_team2': 0,
        }
    )

    form = MatchPredictionForm(request.POST, instance=prediction)
    form.set_team_labels(match.team1, match.team2)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Prediction successful!')
            return redirect('predict:match_list')

    predict_user = Prediction.objects.filter(match=match)

    return render(request, 'predict/predict_match.html', {'match': match, 'form': form, 'predict_user': predict_user})
