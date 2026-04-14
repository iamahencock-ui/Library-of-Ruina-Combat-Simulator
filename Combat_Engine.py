import random
from pages import *
combat_pages={'Light Attack':Combat_Page('Light Attack',2,[{'type':'slash','rolls':[2,3]},{'type':'blunt','rolls':[1,4]}]),
              'Light Defense':Combat_Page('Light Defense',3,[{'type':'evade','rolls':[1,5]},{'type':'block','rolls':[2,3]},{'type':'slash','rolls':[1,2]}])}
def clash(player,enemy):
    clashes=max(player.numdice,enemy.numdice)
    for (int i=)