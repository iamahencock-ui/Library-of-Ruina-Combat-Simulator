import random
from pages import *
combat_pages={'Light Attack':Combat_Page('Light Attack',2,[{'type':'slash','rolls':[2,3]},{'type':'blunt','rolls':[1,4]}]),
              'Light Defense':Combat_Page('Light Defense',3,[{'type':'evade','rolls':[1,5]},{'type':'block','rolls':[2,3]},{'type':'slash','rolls':[1,2]}])}
def clash(player,enemy):
    """
    Calculate the area of a circle.

    Args:
        player (combat_Page): The combat page the player uses
        Enemy (combat_Page): The combat page the npc enemy uses

    Returns:
        list: The results of each individual clash inthe following format [{result:'player'/'enemy'/'tie',damage:int,status_infliction:{status name:int}}]
    """
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
clash()