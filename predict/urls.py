from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('match/<int:match_id>/', views.predict_match, name='predict_match'),
]
