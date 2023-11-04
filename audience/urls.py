from django.urls import path
from . import views

app_name = "audience"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('team_detail/<int:team_id>', views.team_detail, name="team_detail"),
]
