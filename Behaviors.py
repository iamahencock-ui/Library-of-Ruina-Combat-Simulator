import random
class Player:
    def __init__(self):
        self.mhp=35
        self.msp=17
        self.hp=35
        self.sp=17
        self.pages={}
    def action(self):
        temp=[]
        for i in self.pages.keys():
            for j in range(self.pages[i]):
                temp.append(i)
        result=random.choice(temp)
        self.pages[result]-=1
        return result
class NPC:
    '''
    Base NPC template class
    WIP

    hp (int): the max hp of the npc
    sp (int): the max sp of the npc
    pages (dict): the combat bookshelf of the NPC
    '''
    def __init__(self,hp,sp,pages):
        self.mhp=hp
        self.msp=sp
        self.hp=hp
        self.sp=sp
        self.pages=pages
    def action(self):
        temp=[]
        for i in self.pages.keys():
            for j in range(self.pages[i]):
                temp.append(i)
        result=random.choice(temp)
        self.pages[result]-=1
        return result