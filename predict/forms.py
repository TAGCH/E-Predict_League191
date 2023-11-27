from django import forms


class MatchPredictionForm(forms.Form):
    score_team1 = forms.IntegerField(label='Team 1 Score', widget=forms.Select(choices=[(i, i) for i in range(1, 11)]))
    score_team2 = forms.IntegerField(label='Team 2 Score', widget=forms.Select(choices=[(i, i) for i in range(1, 11)]))
