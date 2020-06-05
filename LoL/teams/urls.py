from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='teams-home'),
    path('view', views.teamview, name='team-view'),
    path('size' , views.size, name='team-size'),
    path('reroll', views.reroll, name='team-roll'),
]

