# forms.py
from django import forms
from .models import Prediction


class MatchPredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['score_team1', 'score_team2']

    def set_team_labels(self, team1_name, team2_name):
        self.fields['score_team1'].label = team1_name
        self.fields['score_team2'].label = team2_name
