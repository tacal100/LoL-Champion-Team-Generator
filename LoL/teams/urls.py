from django.urls import path
from . import views

urlpatterns = [
    #path('', PostTeamSize.as_view(), name='teams-home'),
    path('teams/create/', views.teams, name='teams-create'),
    path('', views.home, name='teams-home'),
]

