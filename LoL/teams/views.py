from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Teams

# Create your views here.

teamsize=0
teamamount=0

teamA = [
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
    return render(request, 'teams/main.html', context)

def teams(request):
    print(request.POST)
    global teamsize
    global teamamount
    context = {
        'teamsize':teamsize,
        'teamamount':teamamount,
        'amountofdudes': teamsize*teamamount
    }
    return render(request, 'teams/main.html', context)


class PostTeamSize(ListView):
   
    Teams.objects.all().delete()
    model = Teams
    template_name = 'teams/main.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'teams'

class CreateTeamSize(CreateView):
    model = Teams
    fields=['teamsize','teamamount']

def about(request):
    return HttpResponse('<h1>pipi</h1>')