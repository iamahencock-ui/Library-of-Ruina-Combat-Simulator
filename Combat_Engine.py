import random
from pages import *
combat_pages={'Light Attack':Combat_Page('Light Attack',2,[{'type':'slash','rolls':[2,3]},{'type':'blunt','rolls':[1,4]}]),
              'Light Defense':Combat_Page('Light Defense',3,[{'type':'evade','rolls':[1,5]},{'type':'block','rolls':[2,3]},{'type':'slash','rolls':[1,2]}])}
def clash(player,enemy):
    clashes=max(player.numdice,enemy.numdice)
    result=[]
    for i in range(1,clashes+1):
        if player.numdice>=i and enemy.numdice>=i:
            playerroll=random.randint(player.dice[i-1][0],player.dice[i-1][1])
            enemyroll=random.randint(enemy.dice[i-1][0],enemy.dice[i-1][1])
            if playerroll==enemyroll:
                current='Tie'
            elif playerroll>enemyroll:
                current='Player'
            else:
                current='Enemy'
            