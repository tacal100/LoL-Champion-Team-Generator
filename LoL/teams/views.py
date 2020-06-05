from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Teams
from .teamcreator import splitTeams


# Create your views here.

teamsize=0
teamamount=0
teamlist=[]

def home(request):
    global teamsize
    global teamamount
    if(request.method == 'POST'):
        teamsize = int(request.POST.get('teamsize'))
        teamamount = int(request.POST.get('teamamount'))

    context={
        'teamsize':teamsize,
        'teamamount':teamamount,
        'amountofdudes': teamsize*teamamount
    }
    return render(request, 'teams/main.html', context)

def size(request):
    print(request.POST)
    if(request.method == 'POST'):
        global teamsize
        global teamamount
        teamsize = int(request.POST.get('teamsize'))
        teamamount = int(request.POST.get('teamamount'))
    context = {
        'teamsize':teamsize,
        'teamamount':teamamount,
        'amountofdudes': teamsize*teamamount
    }

    return render(request, 'teams/test.html',context)


def teamview(request):
    print(request.POST)
    global teamsize
    global teamamount
    global teamlist 
    teamlist = list(request.POST.getlist('teammembers'))
    teammembers = splitTeams(teamlist,teamsize,teamamount)
    
    context = {
        'teamsize':teamsize,
        'teamamount':teamamount,
        'amountofdudes': teamsize*teamamount,
        'teams': teammembers
    }
    return render(request, 'teams/teamview.html', context)

def reroll(request):
    global teamsize
    global teamamount
    print(teamlist)
    teammembers = splitTeams(teamlist,teamsize,teamamount)
    context = {
        'teamsize':teamsize,
        'teamamount':teamamount,
        'amountofdudes': teamsize*teamamount,
        'teams': teammembers
    }
    return render(request, 'teams/teamview.html', context)

def about(request):
    return HttpResponse('<h1>pipi</h1>')