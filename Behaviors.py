import random
class Player:
    def __init__(self):
        self.mhp=35
        self.msp=17
        self.hp=35
        self.sp=17
        self.pages={'Light Attack':5,'Light Defense':4}
    def action(self):
        temp=[]
        for i in self.pages.keys():
            for j in range(self.pages[i]):
                temp.append(i)
        result=random.choice(temp)
        self.pages[result]-=1
        return result
class Backstreets_Rat:
    def __init__(self):
        self.mhp=20
        self.msp=7
        self.hp=20
        self.sp=7
        self.pages={'Light Attack':5,'Light Defense':4}
    def action(self):
        temp=[]
        for i in self.pages.keys():
            for j in range(self.pages[i]):
                temp.append(i)
        result=random.choice(temp)
        self.pages[result]-=1
        return result