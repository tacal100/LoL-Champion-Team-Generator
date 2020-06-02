from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

teams = [
    {
        'teamname': 'pp',
        'teammembers': 'Dude 1'
    },{
        'teamname': 'pp2',
        'teammembers': 'Dude 2'
    },
    {
        'teamname': 'pp2',
        'teammembers': 'Dude 3'
    },
    {
        'teamname': 'pp2',
        'teammembers': 'Dude 4'
    },
    {
        'teamname': 'pp2',
        'teammembers': 'Dude 5'
    },
]

def home(request):
    context = {
        'teams': teams
    }
    return render(request, 'teams/main.html', context)

def setTeamSize(request):
    if request.method== 'POST':
        teams = request.Post.get('teamsize')
        print(teams)
    
    return render (request, 'teams/main.html',{'teams': teams} )

def about(request):
    return HttpResponse('<h1>pipi</h1>')