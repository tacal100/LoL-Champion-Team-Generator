from django.db import models

# Create your models here.

class Teams(models.Model):
    teamsize=models.IntegerField(default=5)
    teamamount=models.IntegerField(default=2)

class Team():
    def __init__(self, memberlist):
        self.members = memberlist
