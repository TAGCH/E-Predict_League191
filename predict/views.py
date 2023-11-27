from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Match
from .forms import MatchPredictionForm


def index(request):
    return HttpResponse("Hello, world. You're at the prediction page.")


def match_list(request):
    matches = Match.objects.all()
    return render(request, 'predict/predict_match.html', {'matches': matches})


def predict_match(request, match_id):
    match = Match.objects.get(pk=match_id)

    if request.method == 'POST':
        form = MatchPredictionForm(request.POST)
        if form.is_valid():
            match.score_team1 = form.cleaned_data['score_team1']
            match.score_team2 = form.cleaned_data['score_team2']
            match.save()
            return redirect('match_list')  # Redirect to the match list or another page
    else:
        form = MatchPredictionForm()

    return render(request, 'predict/predict_match.html', {'match': match, 'form': form})
