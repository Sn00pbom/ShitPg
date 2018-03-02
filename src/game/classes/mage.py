from ..player import Player

# from ..inst import spell
class Mage(Player):

    def __init__(self,name,hp,mpMax):
        self.name = name
        self.hp = hp
        self.mpMax = mpMax
        self.mp = mpMax
        # self.spells = loadMageSpells()




    def hasMP(self,amount):
        if amount>self.mp:
            return False
        else:
            return True

def loadMageSpells():
    pass
    # spells = []
    # spells.append(spell.fireball)
    # return spells