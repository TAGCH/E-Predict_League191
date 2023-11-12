from django.urls import path
from . import views

app_name = "audience"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('team_detail/<team_id>', views.team_detail, name="team_detail"),
    path('player_information/<int:player_id>', views.player_information, name="player_information"),
]
