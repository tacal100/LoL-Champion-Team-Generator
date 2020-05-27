from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

teams = [
    {
        'teamname': 'pp',
        'teammembers': 'just me'
    },{
        'teamname': 'pp2',
        'teammembers': 'just you'
    },
]

def home(request):
    context = {
        'teams': teams
    }
    return render(request, 'teams/main.html', context)

def about(request):
    return HttpResponse('<h1>pipi</h1>')