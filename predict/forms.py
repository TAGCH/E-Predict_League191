from django import forms


class MatchPredictionForm(forms.Form):
    match_id = forms.IntegerField(widget=forms.HiddenInput())
    score_team1 = forms.IntegerField(label='Team 1 Score', widget=forms.Select(choices=[(i, i) for i in range(1, 11)]))
    score_team2 = forms.IntegerField(label='Team 2 Score', widget=forms.Select(choices=[(i, i) for i in range(1, 11)]))

    def set_team_labels(self, team1_name, team2_name):
        self.fields['score_team1'].label = team1_name
        self.fields['score_team2'].label = team2_name
