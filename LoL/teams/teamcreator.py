import random
from itertools import islice
from .models import Team

def splitTeams(memberlist, size, amount):
    random.shuffle(memberlist)
    length_to_split = []

    for i in range(amount):
        length_to_split.append(size)

    Inputt = iter(memberlist) 
    Output = [list(islice(Inputt, elem)) 
          for elem in length_to_split] 

    newmembers =[]
    for member in Output:
        newmembers.append(Team(member))
    print(newmembers[0].members)
    return newmembers
            


    